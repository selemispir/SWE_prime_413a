
# Image Processing - Image Classification

## 1. Project Description
This project uses a pretrained machine learning
model to classify images.

## 2. Library
- TensorFlow
- Keras
- NumPy
- Pillow

## 3. Model
MobileNetV2

MobileNetV2 is a convolutional neural network.
It is trained on the ImageNet dataset.

The model can classify images into 1000 classes.

I selected MobileNetV2 because it is lightweight
and easy to use.

## 4. Dataset
The model uses ImageNet pretrained weights.

Input:
- JPG or PNG image
- Image size: 224 x 224 pixels

Output:
- Top 3 predicted classes
- Prediction scores

## 5. Model Evaluation
Test image: dog.jpg

Expected class: Samoyed
Predicted class: Samoyed

Top prediction score: 58.64%

Test result: Passed

This test uses only one image.
More labeled images are needed to measure
the overall model accuracy.

## 6. Implementation
The program:
1. Loads the pretrained MobileNetV2 model.
2. Reads and resizes an image.
3. Preprocesses the image.
4. Predicts the image class.
5. Displays the top 3 predictions.

No model training is required.

## 7. How to Run

Install the libraries:

pip install tensorflow pillow

Run the application:

python 03_image_processing/main.py

Run the test:

python 03_image_processing/test_model.py

## 8. Conclusion
MobileNetV2 successfully classified the test image.

The project shows how to use a pretrained image
classification model without training it.
