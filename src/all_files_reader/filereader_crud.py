import pandas as pd
import scipy.io as sio
import h5py
import pickle
import json
from PIL import Image
import chardet


class DataReader:
    """
    A class for reading data from various file formats.

    Supports: CSV, Excel, JSON, MAT, HDF5, Pickle, JPG images

    Args:
        data_path (str): The path to the data file.

    Raises:
        FileNotFoundError: If the data file is not found.
        IOError: If an error occurs during file reading.
        UnicodeDecodeError: If there's an issue decoding the file's content
            even after chardet detection.
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
            UnicodeDecodeError: If there's an issue decoding the file's content
                even after chardet detection.
        """

        extension = self.data_path.lower()

        try:
            with open(self.data_path, 'rb') as data_file:
                raw_data = data_file.read()
                encoding = chardet.detect(raw_data)['encoding']

            if extension[-4:] == '.csv':
                try:
                    return pd.read_csv(self.data_path, encoding=encoding)
                except UnicodeDecodeError as e:
                    raise UnicodeDecodeError(f"Failed to decode CSV with chardet encoding: {encoding}") from e
            elif extension[-5:] == '.xlsx':
                return pd.read_excel(self.data_path)
            elif extension[-5:] == '.json':
                with open(self.data_path, 'r', encoding=encoding) as json_file:
                    return json.load(json_file)
            elif extension[-4:] == '.mat':
                return sio.loadmat(self.data_path)
            elif extension[-3:] == '.h5':
                with h5py.File(self.data_path, 'r') as hdf5_file:
                    return hdf5_file['data'][:]
            elif extension in ('.pkl', '.jpg', '.jpeg'):
                # Handle supported formats (pickle, jpg, jpeg)
                if extension == '.pkl':
                    with open(self.data_path, 'rb') as pickle_file:
                        return pickle.load(pickle_file)
                elif extension[-4:] == '.jpg' or extension == '.jpeg':
                    return Image.open(self.data_path)
                else:
                    raise ValueError(f"Unsupported file format: {extension}")  # Handle unexpected extensions
            else:
                return 'File Not Accepted'
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found: {self.data_path}")
        except IOError as e:
            raise IOError(f"Error reading data: {str(e)}")
        except UnicodeDecodeError as e:
            raise UnicodeDecodeError(f"Error decoding data with chardet: {str(e)}") from e
