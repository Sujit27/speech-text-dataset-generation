import os
from pathlib import Path
import auditok
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('audio_file_path', type=str, help='directory with all the chunk mp3 files')
args = parser.parse_args()

min_dur = 0.5       # minimum duration of a valid audio event in seconds
max_dur = 8       # maximum duration of an event
max_silence = 0.1   # maximum duration of tolerated continuous silence within an event
energy_threshold = 50 # threshold of detection

output_path = os.path.join(os.path.dirname(args.audio_file_path),"audio_chunks_" + \
    "_" + str(min_dur) + \
    "_" + str(max_dur) + \
    "_" + str(max_silence) + \
    "_" + str(energy_threshold))

Path(output_path).mkdir(parents=True, exist_ok=True)

audio_regions = auditok.split(
    args.audio_file_path,
    min_dur=0.5,     
    max_dur=10,       
    max_silence=max_silence, 
    energy_threshold=energy_threshold
)

for i, r in enumerate(audio_regions):
    filename = r.save(os.path.join(output_path,"region_{meta.start:.3f}-{meta.end:.3f}.wav"))
    print("region saved as: {}".format(filename))
# for i, chunk in enumerate(chunks):
#     print("Segmenting file...chunk{}.wav".format(i))
#     chunk.export(os.path.join(output_path, "chunk{0}.wav".format(i)), format="wav")

# with open(os.path.join(output_path,"metadata.txt"), 'w') as f:
#     for item in silences:
#         f.write("%s\n" % item)