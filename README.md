# Darija Voice Translation

This project transcribes and translates Darija (Moroccan Arabic) audio into text with two main components:

1. **Audio Transcription Model**:Utilizes the Wav2Vec2-large-XLSR-53 model, a state-of-the-art model for speech recognition, fine-tuned on a Darija Dataset, to transcribe audio into accurate text.
2. **Translation Model**: Leverages a fine-tuned version of Helsinki-NLP/opus-mt-ar-en, trained on the None dataset, to translate the transcriptions from Darija into English.

The repository also includes essential tools for collecting data from YouTube videos, including audio and their corresponding transcriptions based on video timestamps. It offers scripts for cleaning, transforming, and organizing the data to make it suitable for training and fine-tuning the the Wav2Vec2-large-XLSR-53 model.

A simple app is also provided that enables users to upload audio files and receive both transcriptions and translations in a straightforward interface.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AnassBe34/darija_data_preprocessing.git
2. Or you can download it manually.
3. Navigate into the project directory:
   ```bash
   cd darija_data_preprocessing
4. Install the required libraries using pip and the requirements.txt file:
   ```bash
   pip install -r requirements.txt
---
## Repository Overview

This repository is mainly composed of three parts:

### 1. Data Preprocessing
In this part, we focus on collecting raw data from YouTube, consisting of long audios with their corresponding transcriptions. We clean and transform this raw data into a format that is trainable for the Wav2Vec2 model.

### 2. Fine-Tuning
In this part, we fine-tune the Wav2Vec2 model on the dataset collected and cleaned in the previous step.

### 3. Final Project App
In this part, we build a simple app that combines:
- The fine-tuned Wav2Vec2 model trained on a Darija dataset.
- A translation model that translates Darija text into English. This is a fine-tuned version of `Helsinki-NLP/opus-mt-ar-en` on the None dataset.

---

## Notes
1. Ensure you update the dataset paths and YouTube video links to your own before running the scripts.
2. If you want to fine-tune the Wav2Vec2 model on your own data, you can skip the data collection scripts but focus on the cleaning scripts for better results.

## Authors

This project is developed and maintained by Anass Benamara and Hossam Tabsissi

## Contact 

- anassbenamara8@gmail.com
- hossam.tab84@gmail.com

