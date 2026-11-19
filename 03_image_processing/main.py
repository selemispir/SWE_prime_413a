
import tensorflow as tf
import numpy as np
from keras.applications import MobileNetV2
from keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from keras.utils import load_img, img_to_array


model = MobileNetV2(weights="imagenet")


image_path = input("Enter image file name: ")


image = load_img(image_path, target_size=(224, 224))
image = img_to_array(image)
image = np.expand_dims(image, axis=0)
image = preprocess_input(image)


predictions = model.predict(image, verbose=0)
results = decode_predictions(predictions, top=3)[0]


for result in results:
    print(result[1], ":", round(result[2] * 100, 2), "%")
