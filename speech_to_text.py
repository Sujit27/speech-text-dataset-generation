import os
import re
import json
import speech_recognition as sr
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_dir', type=str, help='directory with all the chunk mp3 files')
parser.add_argument('language', type=str, help='language code for speech recognition. example hi-In,bn-In')
args = parser.parse_args()

input_file_format = ".wav"
output_json_file = os.path.join(args.input_dir,"text_detected.json")

def atoi(text):
    return int(text) if text.isdigit() else text
def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]  

all_audio_chunks = []
for file in os.listdir(args.input_dir):
    if file.endswith(input_file_format):
        all_audio_chunks.append(file)

all_audio_chunks.sort(key=natural_keys)

output_text_list = []

speech_recognizer = sr.Recognizer()

for file in all_audio_chunks:
    with sr.AudioFile(os.path.join(args.input_dir,file)) as source:
        text = speech_recognizer.listen(source)
        time_start = os.path.splitext(file)[0].split("_")[1].split("-")[0]
        time_end = os.path.splitext(file)[0].split("_")[1].split("-")[1]
    try:
        text_output = speech_recognizer.recognize_google(text,language=args.language) 
        print("Speech to text ...{}".format(file))       
    except:
        text_output = " "
    
    output_text_list.append({'time_start':time_start,'time_end':time_end,'text':text_output})

with open(output_json_file, 'w', encoding='utf8') as f:
    json.dump(output_text_list, f, ensure_ascii=False)


