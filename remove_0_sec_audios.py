from pydub import AudioSegment
import os

nbr = 0

dataset_index = 0

for chunk_index in range(54111) :
    try :
        chunk = AudioSegment.from_file(fr"C:\Users\ASUS\Desktop\dataset\dataset_{dataset_index}\audio_chunk_{chunk_index}.wav")
    except :
        pass
    if chunk.duration_seconds < 1 :
        if os.path.exists(fr"C:\Users\ASUS\Desktop\dataset\dataset_{dataset_index}\audio_chunk_{chunk_index}.wav") :
            os.remove(fr"C:\Users\ASUS\Desktop\dataset\dataset_{dataset_index}\audio_chunk_{chunk_index}.wav")
            os.remove(fr"C:\Users\ASUS\Desktop\dataset\dataset_{dataset_index}\audio_chunk_{chunk_index}.txt")
            print(f"CHUNK AUDIO {chunk_index} FOUND")
            nbr +=1
    if chunk_index % 20000 == 0 and chunk_index!=0:
        dataset_index+=1
print(f"The numbers of 0s audios are : {nbr}")