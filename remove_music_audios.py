import os
def remove_one_word_audios() :
    dataset_index = 0
    nbr = 0
    for chunk_index in range(54111) : ##DONT FORGET TO CHANGE TO YOUR TOTAL CHUNKS
        transcription = fr"C:\Users\ASUS\Desktop\dataset\dataset_{dataset_index}\audio_chunk_{chunk_index}.txt"
        audio = fr"C:\Users\ASUS\Desktop\dataset\dataset_{dataset_index}\audio_chunk_{chunk_index}.wav"
        if os.path.exists(transcription) :
            f = open(transcription, "r", encoding="utf-8")
            content = f.read()
            if content.count('[') >=1 :
                print(chunk_index)
                nbr+=1
                f.close()
                os.remove(transcription)
                os.remove(audio)
        if chunk_index % 20000 == 0 and chunk_index!=0 :
            dataset_index+=1
            
    print(f'the number of music audios deleted are : {nbr}')
remove_one_word_audios()