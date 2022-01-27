from pathlib import Path
import pandas as pd
import numpy as np
import logging
import pickle

from pandas.core.base import PandasObject
from pandas.core.frame import DataFrame
import config
import csv


def _dataReader(path_names: list) -> list:
    '''
    Reads in raw data from .csv files and returns a list

    params:
    ---
    path_names (list): list of all the data files to read in

    returns:
    ---
    sequences (list): raw dataset from data directory
    '''

    sequences = list()

    for name in path_names:
        data = pd.read_csv(name, header=None)
        sequences.append(data.values)

    return sequences


def get_normal_data() -> DataFrame:
    
    if (Path.exists(config.OUTPUT_DATA_DIR+"/normal/normal_data.csv")):
        normal_data = pd.read_csv(config.OUTPUT_DATA_DIR+"/normal/normal_data.csv", header=None)
        return normal_data

    data_list = _dataReader(config.NORMAL_FILES)
    output = np.repeat([1, 1], data_list.lenght() ,axis=0 )

    normal_data = pd.concat(data_list, ignore_index=True)

    normal_data.to_csv()


    return normal_data
    

def get_imbalance_data():
    
    return


def get_horizontal_misalignment_data():

    return


def get_vertical_misalignment_data():

    return


def get_data():

    return

