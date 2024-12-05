import os 

dataset_index = 0
nbr=0
for chunk_index in range(2600, 54111) :
    audio = fr"C:\Users\ASUS\Desktop\dataset\dataset_{dataset_index}\audio_chunk_{chunk_index}_video_end.wav"
    if os.path.exists(audio) :
        for i in range(chunk_index, chunk_index - 50, -1 ) :
            if os.path.exists(fr"C:\Users\ASUS\Desktop\dataset\dataset_{dataset_index}\audio_chunk_{i}.wav") :
                os.remove(fr"C:\Users\ASUS\Desktop\dataset\dataset_{dataset_index}\audio_chunk_{i}.wav")
                os.remove(fr"C:\Users\ASUS\Desktop\dataset\dataset_{dataset_index}\audio_chunk_{i}.txt")
                nbr +=1
                print(i)
    if chunk_index%20000 == 0 and chunk_index !=0 :
        dataset_index+=1
print(f'number of videos that was removed are : {nbr}')