##This file focuses on Unit wise test of each function and class
# will use unittest.Testcases to do the test
# It is a thorough testing

import unittest
import pandas as pd
import json
import h5py
import pickle
from PIL import Image 
import sys 
sys.path.append("./")  
from src.all_files_reader.filereader_crud import DataReader

class TestDataReader(unittest.TestCase):

    def test_read_csv(self):
        """Tests reading a CSV file."""
        data_path = 'tests/test_data/Stocks_data.csv'  
        reader = DataReader(data_path)
        data = reader.read()
        self.assertIsInstance(data, pd.DataFrame)  # Check if data is a pandas DataFrame

if __name__ == '__main__':
    unittest.main()