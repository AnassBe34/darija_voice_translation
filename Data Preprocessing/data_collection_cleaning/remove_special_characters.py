import os
def contains_latine(str) :
    latine_special = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '?', '.', '!', '\\', '-', ';', ':', '"', '“', '%', "'", '�','0',
    '1','2','3','4','5','6','7','8','9',
]
    for letter in latine_special :
        if letter in str :
            return True
    return False

nbr = 0
dataset_index = 0
for chunk_index in range(54111) : ##REPLACE WITH YOUR MAX CHUNK_INDEX
    transc_path = fr"C:\Users\ASUS\Desktop\dataset\dataset_{dataset_index}\audio_chunk_{chunk_index}.txt" ##REPLACE WITH YOUR DATA PATH
    audio_path = fr"C:\Users\ASUS\Desktop\dataset\dataset_{dataset_index}\audio_chunk_{chunk_index}.wav" ##REPLACE WITH YOUR DATA PATH
    if os.path.exists(transc_path) :
        transc_file = open(transc_path, 'r', encoding='utf-8')
        transc = transc_file.read()
        transc_file.close()
        if contains_latine(transc) :
            os.remove(transc_path)
            os.remove(audio_path)
            print(f"Chunk {chunk_index} removed !")
            nbr+=1
    if chunk_index % 20000 == 0 and chunk_index!=0 :
            dataset_index+=1
print(f'The number of latin or special removed audios are {nbr}')