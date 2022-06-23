#!/usr/bin/env python3

import tflite_runtime.interpreter as tflite
# import tensorflow as tf
from data import x_data, y_data
from config import models_path



DATASET_DIR = '/home/italolanza/workspace/TG/dataset/'
DATASET_NAME = 'dataset_completo.csv' 
DATASET_PATH = DATASET_DIR+DATASET_NAME
MODEL_DIR = '/home/italolanza/workspace/TG/graduation-project/models/'
collum_name = ['Tacom_1f0', 'Tacom_2f0', 'Tacom_3f0', 'Tacom_kurtosis', 'Tacom_entropy', 'Aceler_Underhang_X_1f0', 'Aceler_Underhang_X_2f0', 'Aceler_Underhang_X_3f0', 'Aceler_Underhang_X_kurtosis', 'Aceler_Underhang_X_entropy', 'Aceler_Underhang_Y_1f0', 'Aceler_Underhang_Y_2f0', 'Aceler_Underhang_Y_3f0', 'Aceler_Underhang_Y_kurtosis', 'Aceler_Underhang_Y_entropy', 'Aceler_Underhang_Z_1f0', 'Aceler_Underhang_Z_2f0', 'Aceler_Underhang_Z_3f0', 'Aceler_Underhang_Z_kurtosis', 'Aceler_Underhang_Z_entropy', 'Aceler_Overhang_X_1f0', 'Aceler_Overhang_X_2f0', 'Aceler_Overhang_X_3f0', 'Aceler_Overhang_X_kurtosis', 'Aceler_Overhang_X_entropy', 'Aceler_Overhang_Y_1f0', 'Aceler_Overhang_Y_2f0', 'Aceler_Overhang_Y_3f0', 'Aceler_Overhang_Y_kurtosis', 'Aceler_Overhang_Y_entropy', 'Aceler_Overhang_Z_1f0', 'Aceler_Overhang_Z_2f0', 'Aceler_Overhang_Z_3f0', 'Aceler_Overhang_Z_kurtosis', 'Aceler_Overhang_Z_entropy', 'Audio_1f0', 'Audio_2f0', 'Audio_3f0', 'Audio_kurtosis', 'Audio_entropy', 'Class']
all_features = ['Tacom_1f0', 'Tacom_2f0', 'Tacom_3f0', 'Tacom_kurtosis', 'Tacom_entropy', 'Aceler_Underhang_X_1f0', 'Aceler_Underhang_X_2f0', 'Aceler_Underhang_X_3f0', 'Aceler_Underhang_X_kurtosis', 'Aceler_Underhang_X_entropy', 'Aceler_Underhang_Y_1f0', 'Aceler_Underhang_Y_2f0', 'Aceler_Underhang_Y_3f0', 'Aceler_Underhang_Y_kurtosis', 'Aceler_Underhang_Y_entropy', 'Aceler_Underhang_Z_1f0', 'Aceler_Underhang_Z_2f0', 'Aceler_Underhang_Z_3f0', 'Aceler_Underhang_Z_kurtosis', 'Aceler_Underhang_Z_entropy', 'Aceler_Overhang_X_1f0', 'Aceler_Overhang_X_2f0', 'Aceler_Overhang_X_3f0', 'Aceler_Overhang_X_kurtosis', 'Aceler_Overhang_X_entropy', 'Aceler_Overhang_Y_1f0', 'Aceler_Overhang_Y_2f0', 'Aceler_Overhang_Y_3f0', 'Aceler_Overhang_Y_kurtosis', 'Aceler_Overhang_Y_entropy', 'Aceler_Overhang_Z_1f0', 'Aceler_Overhang_Z_2f0', 'Aceler_Overhang_Z_3f0', 'Aceler_Overhang_Z_kurtosis', 'Aceler_Overhang_Z_entropy', 'Audio_1f0', 'Audio_2f0', 'Audio_3f0', 'Audio_kurtosis', 'Audio_entropy']

# load data
# dataset = pd.read_csv(DATASET_PATH, names=collum_name)
# dataset_x = dataset[all_features].values.astype(np.float32)
# dataset_y = dataset['Class'].values.astype(np.uint8)
# x_train, x_test, y_train, y_test = train_test_split(dataset_x, dataset_y, test_size=0.3, shuffle=True)


# Load the TFLite model and allocate tensors.
# interpreter = tf.lite.Interpreter(model_path="converted_model.tflite")
interpreter = tflite.Interpreter(model_path=models_path['tf_lite'])
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
print(f'Input Details: {input_details}')
print(f'Output Detais: {output_details}')

# Test the model on random input data.
input_shape = input_details[0]['shape']
# input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], x_data[:1])

interpreter.invoke()

# The function `get_tensor()` returns a copy of the tensor data.
# Use `tensor()` in order to get a pointer to the tensor.
output_data = interpreter.get_tensor(output_details[0]['index'])
print(f'Tf Lite Model Output: {output_data}')
print(f'Y test Output: {y_data[:1]}')