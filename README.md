# Darija Data Preprocessing

Darija Data Preprocessing is a part of the Darija Speech Recognition project, designed to collect, clean, and transform raw speech data for model training. This repository handles the collection and preprocessing of data from YouTube, improving alignment and preparing it for training the speech recognition model.

---

## Features

### **1. Data Collecting And Transforming**
- **`collect.py`**: Downloads audio files from YouTube, converts their sampling rate to 16 kHz, and splits them into chunks based on the transcription timestamps provided by the video. Each chunk is associated with its corresponding transcription, and the downloaded chunks are stored in a dataset folder within the same project repository.

### 2. Data Cleaning 
- **`delete_extremities.py`**: Removes the extremities of each full audio to reduce misalignments.
- **`delete_long_audios.py`**: Deletes audio chunks longer than 6 seconds to facilitate model training.
- **`one_word_audios.py`**: Removes audio chunks containing only one word, as they are prone to misalignment.
- **`remove_0_sec_audios.py`**: Deletes audio chunks with 0 seconds duration, which are typically disaligned.
- **`remove_music_audios.py`**: Filters out audio chunks with background music, as it is considered noise for the model during training.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AnassBe34/darija_data_preprocessing.git
2. Or you can download it manually.

## Authors

This project is part of the Darija Speech Recognition initiative and is maintained by Anass Benamara and Hossam Tabsissi.

## Contact 

- anassbenamara8@gmail.com
- hossam.tab84@gmail.com

