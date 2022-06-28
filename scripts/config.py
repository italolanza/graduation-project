"""
This file/module contains configuration data used by the other modules
"""

from pathlib import Path
import glob

# DATASET_BASE_DIR = Path("/home/italolanza/workspace/TG/dataset/") # desktop
DATASET_BASE_DIR = Path("/home/italolanza/Workspace/TG/dataset/") # laptop
DATASET_FILE_PATH = DATASET_BASE_DIR.joinpath('dataset_completo.csv')

# NORMAL_FILES = glob.glob(str(DATASET_BASE_DIR) + '/normal/*.csv')

# HOR_MISALIGNMENT_LOW_FILES = glob.glob(str(DATASET_BASE_DIR) + '/horizontal/0.5mm/*.csv')

# HOR_MISALIGNMENT_MEDIUM_FILES = glob.glob(str(DATASET_BASE_DIR) + '/horizontal/1.0mm/*.csv') \
#                                 + glob.glob(str(DATASET_BASE_DIR) + '/horizontal/1.5mm/*.csv')

# HOR_MISALIGNMENT_HIGH_FILES = glob.glob(str(DATASET_BASE_DIR) + '/horizontal/2.0mm/*.csv')

# VER_MISALIGNMENT_LOW_FILES = glob.glob(str(DATASET_BASE_DIR) + '/vertical/0.51mm/*.csv') \
#                                 + glob.glob(str(DATASET_BASE_DIR) + '/vertical/0.63mm/*.csv')

# VER_MISALIGNMENT_MEDIUM_FILES = glob.glob(str(DATASET_BASE_DIR) + '/vertical/1.27mm/*.csv') \
#                                 + glob.glob(str(DATASET_BASE_DIR) + '/vertical/1.40mm/*.csv')

# VER_MISALIGNMENT_HIGH_FILES = glob.glob(str(DATASET_BASE_DIR) + '/vertical/1.78mm/*.csv') \
#                                 + glob.glob(str(DATASET_BASE_DIR) + '/vertical/1.90mm/*.csv')

# IMBALANCE_LOW_FILES = glob.glob(str(DATASET_BASE_DIR) + '/imbalance/6g/*.csv') \
#                         + glob.glob(str(DATASET_BASE_DIR) + '/imbalance/10g/*.csv')

# IMBALANCE_MEDIUM_FILES = glob.glob(str(DATASET_BASE_DIR) + '/imbalance/15g/*.csv') \
#                         + glob.glob(str(DATASET_BASE_DIR) + '/imbalance/20g/*.csv') \
#                         + glob.glob(str(DATASET_BASE_DIR) + '/imbalance/25g/*.csv')

# IMBALANCE_HIGH_FILES = glob.glob(str(DATASET_BASE_DIR) + '/imbalance/30g/*.csv') \
#                         + glob.glob(str(DATASET_BASE_DIR) + '/imbalance/35g/*.csv')

# OUTPUT_DATA_DIR = Path('/home/italolanza/workspace/TG/')
OUTPUT_DATA_DIR = Path('/home/italolanza/Workspace/TG/')

# _models_base_path="/home/italolanza/workspace/TG/graduation-project/models" #desktop
_models_base_path="/home/italolanza/Workspace/TG/graduation-project/models" #laptop
models_path = {
    'onnx': f"{_models_base_path}/onnx/sequential.onnx",
    'tf_lite': f"{_models_base_path}/models/tf_lite/model.tflite",
    'connxr': f"{_models_base_path}/cONNXr/sequential.onnx",
    'keras': f"{_models_base_path}/tf_model/"
}

# _frameworks_base_path = "/home/italolanza/workspace/TG/runtimes" # desktop
_frameworks_base_path = "/home/italolanza/Workspace/TG/runtimes" # laptop
frameworks_path = {
    'connxr': f"{_frameworks_base_path}/cONNXr/"
}