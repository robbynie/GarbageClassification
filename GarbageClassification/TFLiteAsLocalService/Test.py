# By Robbynie

import numpy as np
import tensorflow as tf
from PIL import Image
import requests

# Load lables
with open('labels.txt') as f:
    labels = f.readlines()
labels = [x.strip() for x in labels] 

# Load tflite 
interpreter = tf.lite.Interpreter(model_path="mobilenet_v1_1.0_224.tflite")
interpreter.allocate_tensors()


# Parse the file and get input and output details.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Get the shape of input, to figure out what data we need to input
input_shape = input_details[0]['shape']

print("// Input_data Details are: ")
print("name:", input_details[0]['name'])
print("shape:", input_details[0]['shape'])
print("type:", input_details[0]['dtype'])

# shape: [  1 224 224   3] is data we need to input
#   - 244,244 is size of picture, you can figure this out by referring: ClassifierFloatMobileNet.getImageSizeX() 和 getImageSizeY()
#   - 1 DIM_BATCH_SIZE, refer Classifer.DIM_BATCH_SIZE
#   - 3 DIM_PIXEL_SIZE, refer Classifer.DIM_PIXEL_SIZE
# type: <class 'numpy.float32'>
# index: 0

# Load picture from local, or you can read from REST input from http request
img = Image.open('icecream.jpg')
img.load()
img = img.resize((224, 224), Image.ANTIALIAS)

# Normalize to [0, 1] // Don't know why, Google said it is needed
data = np.asarray( img, dtype="int32" ) / 255.0
# Inference on input data normalized to [0, 1]
input_data = np.expand_dims(data,0).astype(np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)

# Invoke the prediction
interpreter.invoke()

# Get the output details
output_data = interpreter.get_tensor(output_details[0]['index'])

print("// Output Details:")
print("name:", output_details[0]['name'])
print("shape:", output_details[0]['shape'])
print("type:", output_details[0]['dtype'])

print("The result is： Label:{}, Confidence:{:2.0f}%"
      .format(labels[np.argmax(output_data)], 100*output_data[0][np.argmax(output_data)]))
