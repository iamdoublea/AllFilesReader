import os
import sys
from pathlib import Path

import pandas as pd
import numpy as np
import scipy.io as sio
import h5py
import json
import csv
import pickle
from PIL import Image


class DataReader:
        """
    A class for reading data from various file formats.

    Supports: CSV, Excel, JSON, MAT, HDF5, TXT, Pickle, JPG images

    Args:
        data_path (str): The path to the data file.
    """
        def __init__(self,data_path:str):
            self.data_path=data_path


        def read(self):
            """
            Reads the data from the specified file path.

            Returns:
                object: The data loaded from the file, or 'File Not Accepted'
                        if the file format is not supported.
            """
            extension = self.data_path.lower()

            if extension[-4:] == '.csv':
                return pd.read_csv(self.data_path)
            elif extension[-5:] == '.xlsx':
                return pd.read_excel(self.data_path)
            elif extension[-5:] == '.json':
                with open(self.data_path, 'r') as json_file:
                    return json.load(json_file)
            elif extension[-4:] == '.mat':
                return sio.loadmat(self.data_path)
            elif extension[-3:] == '.h5':
                with h5py.File(self.data_path, 'r') as hdf5_file:
                    return hdf5_file['data'][:]
            elif extension in ('.txt', '.py'):  # Handle text and Python files
                with open(self.data_path, 'r') as txt_file:
                    return txt_file.read()
            elif extension[-4:] == '.pkl':
                with open(self.data_path, 'rb') as pickle_file:
                    return pickle.load(pickle_file)
            elif extension[-4:] == '.jpg' or extension == '.jpeg':  # Handle both JPEG extensions
                return Image.open(self.data_path)
            else:
                return 'File Not Accepted'

