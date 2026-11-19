
import numpy as np
from keras.applications import MobileNetV2
from keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from keras.utils import load_img, img_to_array

# Load pretrained model
model = MobileNetV2(weights="imagenet")

# Load image
image = load_img("03_image_processing/dog.jpg", target_size=(224, 224))
image = img_to_array(image)
image = np.expand_dims(image, axis=0)
image = preprocess_input(image)

# Predict
prediction = model.predict(image, verbose=0)
result = decode_predictions(prediction, top=1)[0][0]

# Expected and predicted labels
expected = "Samoyed"
predicted = result[1]

print("Expected:", expected)
print("Predicted:", predicted)

if predicted.lower() == expected.lower():
    print("Test passed!")
else:
    print("Test failed!")
