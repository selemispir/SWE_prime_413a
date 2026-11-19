
# Audio Processing - Speech to Text

## 1. Project Description
This project converts audio into text using a
pretrained machine learning model.

## 2. Library
- OpenAI Whisper
- PyTorch
- JiWER

## 3. Model
Whisper Tiny

Whisper is a speech recognition model.
It converts spoken language into written text.

I selected the Tiny model because it is small,
simple, and suitable for running locally.

## 4. Dataset
The input is an English audio file.

Test file: jfk.flac

The expected transcription is used to
evaluate the model.

## 5. Model Evaluation
Metric: Word Error Rate (WER)

WER measures the number of word errors
compared to the reference text.

Test result:
WER = 0.0%

The model recognized all words correctly
in the selected test audio.

## 6. Implementation
The program:
1. Loads the pretrained Whisper model.
2. Reads an audio file.
3. Converts speech into text.
4. Prints the transcription.

No model training is required.

## 7. How to Run

Install the libraries:

pip install openai-whisper jiwer

FFmpeg must also be installed.

Run the application:

python 02_audio_processing/main.py

Run the test:

python 02_audio_processing/test_model.py

## 8. Conclusion
Whisper Tiny successfully converted the
test audio into text.

The model works locally and does not require
training from scratch.
