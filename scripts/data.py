import sys,os
from pathlib import Path
import glob
import pandas as pd
import numpy as np

# _DATASET_BASE_DIR = Path("/home/italolanza/workspace/TG/dataset/")
_DATASET_BASE_DIR = Path("/home/italolanza/Workspace/TG/dataset")
_DATASET_FILE_PATH = _DATASET_BASE_DIR.joinpath('dataset_completo.csv')
_VALIDATION_INPUT_DATA = _DATASET_BASE_DIR.joinpath('x_test.csv')
_VALIDATION_OUTPUT_DATA = _DATASET_BASE_DIR.joinpath('y_test.csv')

_collum_name = ['Tacom_1f0', 'Tacom_2f0', 'Tacom_3f0', 'Tacom_kurtosis', 'Tacom_entropy', 'Aceler_Underhang_X_1f0', 'Aceler_Underhang_X_2f0', 'Aceler_Underhang_X_3f0', 'Aceler_Underhang_X_kurtosis', 'Aceler_Underhang_X_entropy', 'Aceler_Underhang_Y_1f0', 'Aceler_Underhang_Y_2f0', 'Aceler_Underhang_Y_3f0', 'Aceler_Underhang_Y_kurtosis', 'Aceler_Underhang_Y_entropy', 'Aceler_Underhang_Z_1f0', 'Aceler_Underhang_Z_2f0', 'Aceler_Underhang_Z_3f0', 'Aceler_Underhang_Z_kurtosis', 'Aceler_Underhang_Z_entropy', 'Aceler_Overhang_X_1f0', 'Aceler_Overhang_X_2f0', 'Aceler_Overhang_X_3f0', 'Aceler_Overhang_X_kurtosis', 'Aceler_Overhang_X_entropy', 'Aceler_Overhang_Y_1f0', 'Aceler_Overhang_Y_2f0', 'Aceler_Overhang_Y_3f0', 'Aceler_Overhang_Y_kurtosis', 'Aceler_Overhang_Y_entropy', 'Aceler_Overhang_Z_1f0', 'Aceler_Overhang_Z_2f0', 'Aceler_Overhang_Z_3f0', 'Aceler_Overhang_Z_kurtosis', 'Aceler_Overhang_Z_entropy', 'Audio_1f0', 'Audio_2f0', 'Audio_3f0', 'Audio_kurtosis', 'Audio_entropy', 'Class']
_all_features = ['Tacom_1f0', 'Tacom_2f0', 'Tacom_3f0', 'Tacom_kurtosis', 'Tacom_entropy', 'Aceler_Underhang_X_1f0', 'Aceler_Underhang_X_2f0', 'Aceler_Underhang_X_3f0', 'Aceler_Underhang_X_kurtosis', 'Aceler_Underhang_X_entropy', 'Aceler_Underhang_Y_1f0', 'Aceler_Underhang_Y_2f0', 'Aceler_Underhang_Y_3f0', 'Aceler_Underhang_Y_kurtosis', 'Aceler_Underhang_Y_entropy', 'Aceler_Underhang_Z_1f0', 'Aceler_Underhang_Z_2f0', 'Aceler_Underhang_Z_3f0', 'Aceler_Underhang_Z_kurtosis', 'Aceler_Underhang_Z_entropy', 'Aceler_Overhang_X_1f0', 'Aceler_Overhang_X_2f0', 'Aceler_Overhang_X_3f0', 'Aceler_Overhang_X_kurtosis', 'Aceler_Overhang_X_entropy', 'Aceler_Overhang_Y_1f0', 'Aceler_Overhang_Y_2f0', 'Aceler_Overhang_Y_3f0', 'Aceler_Overhang_Y_kurtosis', 'Aceler_Overhang_Y_entropy', 'Aceler_Overhang_Z_1f0', 'Aceler_Overhang_Z_2f0', 'Aceler_Overhang_Z_3f0', 'Aceler_Overhang_Z_kurtosis', 'Aceler_Overhang_Z_entropy', 'Audio_1f0', 'Audio_2f0', 'Audio_3f0', 'Audio_kurtosis', 'Audio_entropy']

# load dataset
dataset = pd.read_csv(_DATASET_FILE_PATH, names=_collum_name)

# load validation data
_dataset_x = pd.read_csv(_VALIDATION_INPUT_DATA, names=_all_features)
x_data = _dataset_x.values.astype(np.float32)

_dataset_y = pd.read_csv(_VALIDATION_OUTPUT_DATA, names=['Class'])
y_data = _dataset_y.values.astype(np.uint8)

if __name__ == '__main__':
    print(f'Input data path: {_VALIDATION_INPUT_DATA}')
    print(f'Input data shape: {x_data.shape}')
    print(f'Output data path: {_VALIDATION_OUTPUT_DATA}')
    print(f'Output data shape: {y_data.shape}')

# end of file