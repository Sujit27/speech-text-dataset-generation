import os
from pathlib import Path
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.silence import detect_silence
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('mp3_file_path', type=str, help='directory with all the chunk mp3 files')
args = parser.parse_args()

silence_len = 100
silence_threshold = 40

output_path = os.path.join(os.path.dirname(args.mp3_file_path),"audio_chunks_" + str(silence_len) + "_" + str(silence_threshold))
Path(output_path).mkdir(parents=True, exist_ok=True)

sound = AudioSegment.from_mp3(args.mp3_file_path)

chunks = split_on_silence(sound,min_silence_len=silence_len,silence_thresh= - silence_threshold)
silences = detect_silence(sound,min_silence_len=silence_len,silence_thresh= - silence_threshold)

for i, chunk in enumerate(chunks):
    print("Segmenting file...chunk{}.wav".format(i))
    chunk.export(os.path.join(output_path, "chunk{0}.wav".format(i)), format="wav")

with open(os.path.join(output_path,"metadata.txt"), 'w') as f:
    for item in silences:
        f.write("%s\n" % item)