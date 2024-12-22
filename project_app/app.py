import streamlit as st
import librosa
import torch
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM




@st.cache_resource  # Cache the model and processor to avoid reloading on each interaction
def load_model():
    processor = Wav2Vec2Processor.from_pretrained("boumehdi/wav2vec2-large-xlsr-moroccan-darija")
    model = Wav2Vec2ForCTC.from_pretrained("boumehdi/wav2vec2-large-xlsr-moroccan-darija")
    return processor, model

processor, model = load_model()


st.title("Moroccan Darija Speech-to-Text")
st.write("Upload an audio file to transcribe.")


uploaded_file = st.file_uploader("Choose a WAV file", type=["wav"])

if uploaded_file:

    st.audio(uploaded_file, format="audio/wav")


    st.write("Processing audio...")
    input_audio, sr = librosa.load(uploaded_file, sr=16000)


    input_values = processor(input_audio, return_tensors="pt", padding=True).input_values


    with torch.no_grad():  
        logits = model(input_values).logits


    tokens = torch.argmax(logits, axis=-1)
    transcription = processor.batch_decode(tokens, skip_special_tokens=True)


    st.subheader("Transcription:")
    st.write(transcription[0])
    
    tokenizer1 = AutoTokenizer.from_pretrained("centino00/darija-to-english")
    model1 = AutoModelForSeq2SeqLM.from_pretrained("centino00/darija-to-english")

    input_ids = tokenizer1(transcription[0], return_tensors="pt").input_ids 
    generated_ids = model1.generate(input_ids)
    output = tokenizer1.decode(generated_ids[0], skip_special_tokens=True)
    
    st.subheader("Translation:")
    st.write(output)
    
    
