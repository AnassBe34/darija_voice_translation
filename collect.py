import yt_dlp as youtube_dl  # Now using yt-dlp for better support
import os
from pydub import AudioSegment
from youtube_transcript_api import YouTubeTranscriptApi




url_list = [
    'https://www.youtube.com/watch?v=N8VbED0CPXc',
'https://www.youtube.com/watch?v=ikUHqsSZROQ',
'https://www.youtube.com/watch?v=sEehKE0dhps',
'https://www.youtube.com/watch?v=25F5WHlX1-c',
'https://www.youtube.com/watch?v=dYBsyOzJ4eM',
'https://www.youtube.com/watch?v=BtynNJRZ38E',
'https://www.youtube.com/watch?v=0GH4aOSuVrE',
'https://www.youtube.com/watch?v=icSK1ZH3FxQ',
'https://www.youtube.com/watch?v=VdD7IYEn4UQ',
'https://www.youtube.com/watch?v=if16s8GaHuw',
'https://www.youtube.com/watch?v=yd2iBBPEkZg',
'https://www.youtube.com/watch?v=yI8WOq-F4Dk',
'https://www.youtube.com/watch?v=gqAur5NCQxk',
'https://www.youtube.com/watch?v=mvZQOvpCB-I',
'https://www.youtube.com/watch?v=zZee9UqTDoM',
'https://www.youtube.com/watch?v=SiMj4gOpbiY',
'https://www.youtube.com/watch?v=TUACReYT3gI',
'https://www.youtube.com/watch?v=_m4F-7-PXtk',
'https://www.youtube.com/watch?v=3otr0eUgAFg',
'https://www.youtube.com/watch?v=cdCVEa5RYXQ',
'https://www.youtube.com/watch?v=fUOG1JaQZWg',
'https://www.youtube.com/watch?v=R7Roz4Pjzj0',
'https://www.youtube.com/watch?v=ymed8hH94v4',
'https://www.youtube.com/watch?v=AIXcZoIAeCM',
'https://www.youtube.com/watch?v=pa6WHYDiU4A',
'https://www.youtube.com/watch?v=Uo1a0ZORpRs',
'https://www.youtube.com/watch?v=Po_mE7Z42-4',
'https://www.youtube.com/watch?v=3XYTgt8FjBM',
'https://www.youtube.com/watch?v=TvF4DHLDGdk',
'https://www.youtube.com/watch?v=M8J4JlMoaC4',
'https://www.youtube.com/watch?v=ecHhNT-_DY8',
'https://www.youtube.com/watch?v=E6lKNEW4Oic',
'https://www.youtube.com/watch?v=3p3hyixOstg',
'https://www.youtube.com/watch?v=PVZni5BZeF4',
'https://www.youtube.com/watch?v=wczpq6elPLs',
'https://www.youtube.com/watch?v=nIUHlPI8zT0',
'https://www.youtube.com/watch?v=dU9FxSgnOQA',
'https://www.youtube.com/watch?v=fWPheh9p-FA',
'https://www.youtube.com/watch?v=jQKYMyK1qOs',
'https://www.youtube.com/watch?v=bqTw6Iqar8I',
'https://www.youtube.com/watch?v=dN8IOezKKBE',
'https://www.youtube.com/watch?v=7LbpUGjprRs',
'https://www.youtube.com/watch?v=vnkuNNqRMRc'
]


def download_audio(yt_url, folder_name, audio_name):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{folder_name}/{audio_name}',  # Save without .mp3 extension
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt_url])
        print(f"Audio downloaded for {yt_url} and saved as {audio_name} in {folder_name}")
    except Exception as e:
        print(f"An error occurred while downloading audio: {e}")
        
def convert_to_wav(folder_name, audio_name):
    input_file = f"{folder_name}/{audio_name}.mp3"
    output_file = f"{folder_name}/{audio_name}.wav"
    
    # Load and convert the audio file
    audio = AudioSegment.from_mp3(input_file)
    audio.export(output_file, format="wav")
    
    # Remove the original .mp3 file
    if os.path.exists(output_file):
        os.remove(input_file)
        print(f"Conversion complete! '{input_file}' has been replaced by '{output_file}'.")
    else:
        print("Conversion failed; .wav file was not created.")
        


def cut_audio(input_file, output_file, start_time, end_time):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Cut the audio
    cut_audio = audio[start_time:end_time]

    # Save the cut audio to a new file
    cut_audio.export(output_file, format = 'wav')

def get_starts(video_id) :
    transcription = YouTubeTranscriptApi.get_transcript(video_id,  languages=['ar'])
    starts = []
    for element in transcription :
        starts.append(element['start'])
    return starts

def get_ends(video_id) :
    transcription = YouTubeTranscriptApi.get_transcript(video_id,  languages=['ar'])
    ends = []
    for element in transcription :
        ends.append(element['start'] + element['duration'])
    return ends

def get_transcriptions(video_id) :
    transcription = YouTubeTranscriptApi.get_transcript(video_id,  languages=['ar'])
    transcriptions = []
    for element in transcription :
        transcriptions.append(element['text'])
    return transcriptions



def get_video_id(url) :
    id = url.rsplit("=")
    return id[1]



def process_videos(url_list):
    global_chunk_index = 33026
    datasets_index = 1
    # Make the first dataset folder in case you still don't have the first one
    #os.mkdir(fr'dataset\dataset_{datasets_index}')
    for i, url in enumerate(url_list, start=0):
        folder_name = f"dataset"
        audio_name = f"audio_{i}"
        audio_file = fr'dataset\audio_{i}.mp3'
        transcription_name = f"transcription_{i}"
        
        # download audio and save as .mp3 without extension in name
        download_audio(url, folder_name, audio_name)
        
        
        #change sampling rate to 16khz
        audio_mp3 = AudioSegment.from_file(audio_file)
        resampled_audio = audio_mp3.set_frame_rate(16000)
        resampled_audio.export(audio_file, format="mp3")
        # Convert the audio to .wav
        convert_to_wav(folder_name, audio_name)
        
        input_file = fr'dataset\audio_{i}.wav'
        video_id = get_video_id(url)
        transcriptions = get_transcriptions(video_id)
        starts = get_starts(video_id)
        ends = get_ends(video_id)
        for j in range(len(starts)) :
            output_file = fr'dataset\dataset_{datasets_index}\audio_chunk_{global_chunk_index}.wav'
            start_time = starts[j] * 1000 - 150
            if start_time<0 :
                start_time += 150
            if j + 1 < len(starts) :
                end_time = starts[j + 1] * 1000 + 150
                output_file = fr'dataset\dataset_{datasets_index}\audio_chunk_{global_chunk_index}.wav'
                text_file = fr'dataset\dataset_{datasets_index}\audio_chunk_{global_chunk_index}.txt'
            else : 
                end_time = ends[j] * 1000
                output_file = fr'dataset\dataset_{datasets_index}\audio_chunk_{global_chunk_index}_video_end.wav'
                text_file = fr'dataset\dataset_{datasets_index}\audio_chunk_{global_chunk_index}_video_end.txt'
            '''           
            print('##########################################')
            print(f"start of the audio is {start_time}")
            print(f"end of the audio is {end_time}")
            print('##########################################')
            '''
            cut_audio(input_file, output_file, start_time, end_time)
            f = open(text_file, "x", encoding="utf-8") ## utf-8 for arabic text
            f.write(transcriptions[j])
            f.close()
            # chunk created -> chunk index needs to be increased
            global_chunk_index+=1
            #checks if we have reached 20k chunks to create a new dataset folder
            if global_chunk_index % 20000 == 0 :
                datasets_index+=1
                os.mkdir(fr'dataset\dataset_{datasets_index}')
            
        os.remove(fr'dataset\audio_{i}.wav')
        

## continue from audio 15 (it is not )


if __name__ == "__main__":
    process_videos(url_list)
