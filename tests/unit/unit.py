##This file focuses on Unit wise test of each function and class
# will use unittest.Testcases to do the test
# It is a thorough testing

import unittest
import pandas as pd
import json
import h5py
from io import open  
import pickle
from PIL import Image  
from scipy.io import sio  
from src.all_files_reader.filereader_crud import DataReader  # Assuming data_reader.py is in src folder

class TestDataReader(unittest.TestCase):

    def test_read_csv(self):
        """Tests reading a CSV file."""
        data_path = 'data.csv'  # Replace with your test CSV file path
        reader = DataReader(data_path)
        data = reader.read()
        self.assertIsInstance(data, pd.DataFrame)  # Check if data is a pandas DataFrame

    def test_read_json(self):
        """Tests reading a JSON file."""
        data_path = 'data.json'  # Replace with your test JSON file path
        reader = DataReader(data_path)
        data = reader.read()
        self.assertIsInstance(data, dict)  # Check if data is a dictionary

    def test_unsupported_format(self):
        """Tests handling of unsupported file format."""
        data_path = 'data.unsupported'
        reader = DataReader(data_path)
        data = reader.read()
        self.assertEqual(data, 'File Not Accepted')  # Check for expected error message

if __name__ == '__main__':
    unittest.main()