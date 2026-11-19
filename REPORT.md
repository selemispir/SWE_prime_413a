
# Machine Learning Applications Report

## 1. Introduction

The objective of this project is to learn how to use
pretrained machine learning models for different tasks.

Five applications were developed:
1. Text Processing
2. Audio Processing
3. Image Processing
4. Video Processing
5. Local Large Language Model

All models were used without additional training.

## 2. Text Processing

### Task
Classify English sentences as positive or negative.

### Library
Hugging Face Transformers and PyTorch.

### Model
DistilBERT, fine-tuned on the SST-2 dataset.

The model analyzes the text and predicts its sentiment.

### Advantages
- Easy to use
- Pretrained model
- Simple Python implementation

### Dataset
Input: English sentences.

The test dataset contains 10 labeled sentences
with POSITIVE and NEGATIVE labels.

### Evaluation
Metric: Accuracy.

Accuracy = Correct predictions / Total predictions.

The model was tested using 10 sentences.

### Implementation
The application loads the pretrained model,
receives text input, and displays the prediction
with a confidence score.

## 3. Audio Processing

### Task
Convert spoken English into written text.

### Library
OpenAI Whisper, PyTorch, and JiWER.

### Model
Whisper Tiny.

Whisper uses an encoder-decoder Transformer
architecture for speech recognition.

### Advantages
- Small model
- Supports multiple languages
- Runs locally

### Dataset
Input: JFK speech audio file in FLAC format.

Reference text is used for evaluation.

### Evaluation
Metric: Word Error Rate (WER).

Test result: WER = 0.0%.

This result was obtained using one short audio file.
It does not represent general model accuracy.

### Implementation
The model reads an audio file, recognizes speech,
and prints the transcription.

FFmpeg is used for audio processing.

## 4. Image Processing

### Task
Identify objects in an image.

### Library
TensorFlow and Keras.

### Model
MobileNetV2.

MobileNetV2 is a convolutional neural network
trained on ImageNet.

### Advantages
- Lightweight model
- Fast inference
- Easy integration with Keras

### Dataset
Input: JPG image resized to 224 x 224 pixels.

The pretrained model uses ImageNet classes.

### Evaluation
Test image: dog.jpg.

Expected class: Samoyed.
Predicted class: Samoyed.

Top prediction score: 58.64%.

The single-image test passed.

### Implementation
The application loads an image, preprocesses it,
and displays the three most likely classes.

## 5. Video Processing

### Task
Detect objects in a video.

### Library
Ultralytics YOLO and PyTorch.

### Model
YOLO11n.

YOLO detects objects and their positions
using bounding boxes.

### Advantages
- Fast object detection
- Pretrained model
- Supports video processing

### Dataset
Input: MP4 video file.

The video is processed frame by frame.

### Evaluation
Frames processed: 62.
Total detections: 971.

The test video contains people detected by YOLO.

The total detection count may include the same
person in multiple frames.

Precision, Recall, and mAP could be measured
using manually labeled video frames.

### Implementation
The application reads a video, detects objects,
and saves a new video with bounding boxes.

## 6. Local Large Language Model

### Task
Generate answers to text questions locally.

### Library
Ollama and Ollama Python library.

### Model
Qwen3 1.7B.

Qwen3 is a Transformer-based language model.

### Advantages
- Runs locally
- Does not require cloud inference
- Small model size

### Dataset
Input: User questions in text format.

Output: Generated text responses.

No additional training dataset is required.

### Evaluation
The model was tested with three questions
about Python, machine learning, and AI.

Evaluation methods:
- Response time
- Answer relevance
- Answer correctness

One observed response time was 2.91 seconds.

### Implementation
The Python program sends user questions
to the local Ollama model and prints the answers.

## 7. Framework Comparison

The project uses several machine learning tools:

- Hugging Face Transformers
- PyTorch
- TensorFlow / Keras
- Ultralytics YOLO
- Ollama

These tools simplify the development of AI applications
because pretrained models are already available.

## 8. Conclusion

This project demonstrates the use of pretrained
machine learning models for five different tasks.

The applications process text, audio, images,
video, and natural language questions.

No model training or fine-tuning was required.

All applications were executed locally.

The project helped me understand how existing
machine learning libraries can solve practical problems.
