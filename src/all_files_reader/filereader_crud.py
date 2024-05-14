import pandas as pd
import scipy.io as sio
import h5py
import json
import csv
import pickle
from PIL import Image


class DataReader:
    """
    A class for reading data from various file formats.

    Supports: CSV, Excel, JSON, MAT, HDF5, TXT (with encoding detection), Pickle, JPG images

    Args:
        data_path (str): The path to the data file.

    Raises:
        FileNotFoundError: If the data file is not found.
        IOError: If an error occurs during file reading.
        UnicodeDecodeError: If there's an issue decoding the file's content.
    """

    def __init__(self, data_path: str):
        self.data_path = data_path

    def read(self) -> object:
        """
        Reads the data from the specified file path.

        Returns:
            object: The data loaded from the file, or 'File Not Accepted'
                    if the file format is not supported.

        Raises:
            FileNotFoundError: If the data file is not found.
            IOError: If an error occurs during file reading.
            UnicodeDecodeError: If there's an issue decoding the file's content.
        """

        extension = self.data_path.lower()

        try:
            if extension[-4:] == '.csv':
                # Try UTF-8 first, then attempt common encodings if it fails
                try:
                    return pd.read_csv(self.data_path, encoding="utf-8")
                except UnicodeDecodeError:
                    encodings = ["latin-1", "cp1252", "ISO-8859-1"]
                    for encoding in encodings:
                        try:
                            return pd.read_csv(self.data_path, encoding=encoding)
                        except UnicodeDecodeError:
                            pass
                    raise UnicodeDecodeError("Failed to decode CSV with common encodings")
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
            elif extension in ('.txt', '.py'):
                # Detect encoding using chardet library (optional)
                # You might need to install chardet (`pip install chardet`)
                # from chardet import detect
                # with open(self.data_path, 'rb') as txt_file:
                #     rawdata = txt_file.read()
                #     result = detect(rawdata)
                #     encoding = result['encoding'] if result['encoding'] is not None else 'utf-8'
                #     return txt_file.read().decode(encoding)
                with open(self.data_path, 'r', encoding="utf-8") as txt_file:
                    try:
                        return txt_file.read()
                    except UnicodeDecodeError:
                        # Optional: Fallback to reading in binary mode for non-text files
                        with open(self.data_path, 'rb') as binary_file:
                            return binary_file.read()
            elif extension[-4:] == '.pkl':
                with open(self.data_path, 'rb') as pickle_file:
                    return pickle.load(pickle_file)
            elif extension[-4:] == '.jpg' or extension == '.jpeg':
                return Image.open(self.data_path)
            else:
                return 'File Not Accepted'
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found: {self.data_path}")
        except (IOError, UnicodeDecodeError) as e:
            raise IOError(f"Error reading data: {str(e)}")
