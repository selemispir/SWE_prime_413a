
# Video Processing - Object Detection

## 1. Project Description
This project detects objects in videos using
a pretrained machine learning model.

## 2. Library
- Ultralytics YOLO
- PyTorch

## 3. Model
YOLO11n

YOLO is an object detection model.
It can identify objects and their locations
in video frames.

I selected YOLO11n because it is small,
fast, and easy to use.

## 4. Dataset
The model uses pretrained weights.

Input:
- MP4 video file

Output:
- Video with bounding boxes
- Object class labels
- Confidence scores

## 5. Model Evaluation
Test video: test_video.mp4

Frames processed: 62
Total detections: 971

The model detected people in the video.

The detection count includes objects detected
in different frames. The same person may be
detected more than once.

These results do not measure model accuracy.
Labeled video frames would be needed to
calculate Precision, Recall, and mAP.

## 6. Implementation
The program:
1. Loads the pretrained YOLO11n model.
2. Reads the video file.
3. Detects objects in each frame.
4. Draws bounding boxes around objects.
5. Saves the processed video.

No model training is required.

## 7. How to Run

Install the library:

pip install ultralytics

Run the application:

python 04_video_processing/main.py

Run the test:

python 04_video_processing/test_model.py

## 8. Conclusion
YOLO11n successfully detected objects in
the test video.

The model works locally without training.
