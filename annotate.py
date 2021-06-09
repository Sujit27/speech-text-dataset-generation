import os
import json
import re
import argparse
import indicnlp.tokenize.indic_tokenize as tk

parser = argparse.ArgumentParser()
parser.add_argument('output_from_pdf', type=str, help='text file from transcription pdf')
parser.add_argument('output_from_speech', type=str, help='json file from speech sementation and recognition')
args = parser.parse_args()

def word_tokenize(sentence):
    wordlst = []
    for word in tk.trivial_tokenize(sentence): 
        if(len(word)>3):
            wordlst.append(word)
    return(wordlst)

def search_word_in_text_list(word,text_list,search_start_index):
    index_found = None
    search_start_index += 1
    text_list = text_list[search_start_index:]
    for i,text in enumerate(text_list):
        if text.find(word) != -1:
          index_found = search_start_index + i
          break

    return index_found  

class Annotator():
    '''
    annotates the audio to the text transcription
    '''
    def __init__(self,original_transcription_file,generated_transcription_file):
        self.original_transcription = self.txt_to_list(original_transcription_file)
        self.generated_transcription = self.json_to_list(generated_transcription_file)
        self.generated_transcription = self.cleanup_generated_transcription()
        self.processed_transcription = []
        self.current_text_index = 0
        self.output_file = os.path.join(os.path.dirname(generated_transcription_file),"text_detected_processed.json")

    def txt_to_list(self,file):
        with open(file) as f:
            transcription = f.readlines()
        transcription = [x.strip() for x in transcription]
        return transcription

    def json_to_list(self,file):
        with open(file) as f:
            transcription = json.load(f)
        return transcription

    def cleanup_generated_transcription(self):
        transcription = [item for item in self.generated_transcription if item['text'] != " "]
        return transcription

    def set_text_index_for_speech(self,generated_dict):
        word_list = word_tokenize(generated_dict["text"])
        for word in word_list:
            text_index_found = search_word_in_text_list(word,self.original_transcription,self.current_text_index)
            if text_index_found:
                self.current_text_index = text_index_found
                processed_dict = {'time_start':generated_dict["time_start"],\
                                'time_end':generated_dict["time_end"],\
                                'text':self.original_transcription[self.current_text_index]}
                self.processed_transcription.append(processed_dict)
                break
            else:
                continue


    def annotate(self):
        for dict in self.generated_transcription:
            self.set_text_index_for_speech(dict)

        with open(self.output_file, 'w', encoding='utf8') as f:
            json.dump(self.processed_transcription, f, ensure_ascii=False)


if __name__ == "__main__":
    annotator = Annotator(args.output_from_pdf,args.output_from_speech)
    annotator.annotate()



