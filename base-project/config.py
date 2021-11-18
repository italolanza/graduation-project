"""
This file/module contains configuration data used by the other modules
"""

from pathlib import Path
import glob


# Path related configuration
DATASET_BASE_DIR = Path("/home/italolanza/workspace/TG/dataset")

NORMAL_FILES = glob.glob(str(DATASET_BASE_DIR) + '/normal/*.csv')

HOR_MISALIGNMENT_LOW_FILES = glob.glob(str(DATASET_BASE_DIR) + '/horizontal/0.5mm/*.csv')

HOR_MISALIGNMENT_MEDIUM_FILES = glob.glob(str(DATASET_BASE_DIR) + '/horizontal/1.0mm/*.csv') \
                                + glob.glob(str(DATASET_BASE_DIR) + '/horizontal/1.5mm/*.csv')

HOR_MISALIGNMENT_HIGH_FILES = glob.glob(str(DATASET_BASE_DIR) + '/horizontal/2.0mm/*.csv')

VER_MISALIGNMENT_LOW_FILES = glob.glob(str(DATASET_BASE_DIR) + '/vertical/0.51mm/*.csv') \
                                + glob.glob(str(DATASET_BASE_DIR) + '/vertical/0.63mm/*.csv')

VER_MISALIGNMENT_MEDIUM_FILES = glob.glob(str(DATASET_BASE_DIR) + '/vertical/1.27mm/*.csv') \
                                + glob.glob(str(DATASET_BASE_DIR) + '/vertical/1.40mm/*.csv')

VER_MISALIGNMENT_HIGH_FILES = glob.glob(str(DATASET_BASE_DIR) + '/vertical/1.78mm/*.csv') \
                                + glob.glob(str(DATASET_BASE_DIR) + '/vertical/1.90mm/*.csv')

IMBALANCE_LOW_FILES = glob.glob(str(DATASET_BASE_DIR) + '/imbalance/6g/*.csv') \
                        + glob.glob(str(DATASET_BASE_DIR) + '/imbalance/10g/*.csv')

IMBALANCE_MEDIUM_FILES = glob.glob(str(DATASET_BASE_DIR) + '/imbalance/15g/*.csv') \
                        + glob.glob(str(DATASET_BASE_DIR) + '/imbalance/20g/*.csv') \
                        + glob.glob(str(DATASET_BASE_DIR) + '/imbalance/25g/*.csv')

IMBALANCE_HIGH_FILES = glob.glob(str(DATASET_BASE_DIR) + '/imbalance/30g/*.csv') \
                        + glob.glob(str(DATASET_BASE_DIR) + '/imbalance/35g/*.csv')

OUTPUT_DATA_DIR = Path('./checkpoints')
OUTPUT_DATA_FILE = OUTPUT_DATA_DIR / Path('raw_data.p')