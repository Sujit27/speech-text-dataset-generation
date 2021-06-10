import os
import json
import re
import argparse
from collections import OrderedDict
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
        self.output_file = os.path.join(os.path.dirname(generated_transcription_file),"text_detected_v1.json")

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

    def __map_speech_to_text(self,speech_index,text_index):
        speech_text_dict = OrderedDict() # a speech index key is mapped to list of indices matched in text
        speech_search_window = 3 # this many number of subsequent speech dicts will be probed to look for many-one mappings etc
        text_indices_tolerance = 2 # this much diff allowed for text index search for words of a specific speech, index will be ignored if exceeds this value
        for i in range(speech_search_window):
            if speech_index + i < len(self.generated_transcription):
                speech = self.generated_transcription[speech_index+i]['text']
                word_list = word_tokenize(speech)
                text_indices = set()
                for word in word_list:
                    text_index_found = search_word_in_text_list(word,self.original_transcription,text_index)
                    if text_index_found and (not text_indices):
                        text_indices.add(text_index_found)
                    elif text_index_found and text_indices:
                        if text_index_found < max(text_indices) + text_indices_tolerance:
                            text_indices.add(text_index_found)
                        
                speech_text_dict[speech_index+i] = text_indices

        if not speech_text_dict[speech_index]:
            return 'one-none',{speech_index},None
        else:
            speech_indices_final = {speech_index}
            text_indices_final = speech_text_dict.pop(speech_index)
            for key,val in speech_text_dict.items():
                if not val:
                    speech_indices_final.add(key)
                elif text_indices_final.intersection(val):
                    speech_indices_final.add(key)
                    text_indices_final.update(val)
        if len(speech_indices_final) == 1 and len(text_indices_final) == 1:
            return 'one-one',speech_indices_final, text_indices_final
        elif len(speech_indices_final) == 1 and len(text_indices_final) > 1:
            return 'one-many',speech_indices_final, text_indices_final
        elif len(speech_indices_final) > 1 and len(text_indices_final) == 1:
            return 'many-one',speech_indices_final, text_indices_final
        elif len(speech_indices_final) > 1 and len(text_indices_final) > 1:
            return 'many-many',speech_indices_final, text_indices_final


    def annotate(self):
        speech_index = 0
        text_index = 0
        while speech_index < len(self.generated_transcription):
            dict = self.generated_transcription[speech_index]
            speech_text_mapping,speech_indices_set,text_indices_set = self.__map_speech_to_text(speech_index,text_index)
            
            if speech_text_mapping == 'one-one':
                text = self.original_transcription[min(text_indices_set)]
                processed_dict = {'time_start':dict["time_start"],'time_end':dict["time_end"],'text':text}
                self.processed_transcription.append(processed_dict)
                speech_index += 1
                text_index += 1
            elif speech_text_mapping == 'one-many':
                text = " ".join(self.original_transcription[index] for index in text_indices_set)
                processed_dict = {'time_start':dict["time_start"],'time_end':dict["time_end"],'text':text}
                self.processed_transcription.append(processed_dict)
                speech_index += 1
                text_index += len(text_indices_set)
            elif speech_text_mapping == 'many-one':
                last_dict = self.generated_transcription[max(speech_indices_set)]
                text = self.original_transcription[min(text_indices_set)]
                processed_dict = {'time_start':dict["time_start"],'time_end':last_dict["time_end"],'text':text}
                self.processed_transcription.append(processed_dict)
                speech_index += len(speech_indices_set)
                text_index += 1
            elif speech_text_mapping == 'many-many':
                last_dict = self.generated_transcription[max(speech_indices_set)]
                text = " ".join(self.original_transcription[index] for index in text_indices_set)
                processed_dict = {'time_start':dict["time_start"],'time_end':last_dict["time_end"],'text':text}
                self.processed_transcription.append(processed_dict)
                speech_index += len(speech_indices_set)
                text_index += len(text_indices_set)
            elif speech_text_mapping == 'one-none':
                processed_dict = {'time_start':dict["time_start"],'time_end':dict["time_end"],'text':" "}
                self.processed_transcription.append(processed_dict)
                speech_index += len(speech_indices_set)
            else:
                speech_index += 1
            

    def save_annotation(self):
        with open(self.output_file, 'w', encoding='utf8') as f:
            json.dump(self.processed_transcription, f, ensure_ascii=False)


if __name__ == "__main__":
    annotator = Annotator(args.output_from_pdf,args.output_from_speech)
    annotator.annotate()
    annotator.save_annotation()



