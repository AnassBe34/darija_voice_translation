import os
from pydub import AudioSegment

f = open('test.txt', 'w', encoding="utf-8")
f.write('path|transcript\n')
for chunk_index in range(1500, 1900) :
    audio_path = fr"C:\Users\ASUS\Desktop\dataset\dataset_0\audio_chunk_{chunk_index}.wav"
    transcription_path = fr"C:\Users\ASUS\Desktop\dataset\dataset_0\audio_chunk_{chunk_index}.txt"
    if os.path.exists(audio_path) :
        audio = AudioSegment.from_file(audio_path)
        duration = audio.duration_seconds
        trans_file = open(transcription_path, 'r', encoding="utf-8")
        transcription = trans_file.read()
        trans_file.close()
        f.write(f"{audio_path}|")
        f.write(f"{transcription}\n")
        #f.write(f"{duration}\n")
        
f.close()
    
