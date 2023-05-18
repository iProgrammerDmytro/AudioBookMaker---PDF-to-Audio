# AudioBookMaker - PDF to Audio

## Project Overview

The AudioBookMaker is a Python project that converts PDF files to audio. It provides an easy-to-use graphical user interface that allows users to select a PDF file and then convert the contents into spoken text. This project is particularly useful for people who wish to consume written content in audio format.

This tool is beneficial for visually impaired individuals, for those who want to convert their books to audiobooks, or even for those who want to listen to articles, documents, or books while doing other tasks.

The project is modularized into three separate modules for better maintainability and separation of concerns.

## Modules

* text_to_speech_thread.py: This module contains the TextToSpeechThread class, which is a subclass of the Thread class. It converts a given text to speech, and handles the playing and stopping of the audio.

* audio_player.py: This module contains the AudioPlayer class, which handles the playback of audio files. It provides methods to play and stop the audio.

* main_app.py: This module creates the graphical user interface and integrates the functions provided by TextToSpeechThread and AudioPlayer. It provides buttons for the user to select a PDF, play the audio, and stop the playback.

## Libraries Used

The project uses several Python libraries:

* tkinter for creating the graphical user interface.
* threading for handling concurrent operations.
* tempfile for generating temporary files.
* PyPDF2 for handling PDF files.
* gTTS (Google Text-to-Speech) for converting text into speech.
* pygame for audio playback.

## Getting Started

To use the AudioBookMaker, clone the repository, install the required Python libraries listed in the requirements.txt file, and run the main_app.py file.
