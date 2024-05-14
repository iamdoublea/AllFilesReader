#To make sure that the package works well in real world situation, on an overall basis
#To make sure all the components are working well with each other

import os
import sys

sys.path.append("./")
from all_files_reader.filereader_crud import DataReader


def test_data_reader_integration():
    """Tests DataReader with actual file reading (integration test).

    This test assumes sample data files exist in a specific location.
    You may need to adjust paths or create sample files.
    """

    # Test CSV
    data_path = os.path.join('tests/test_data', 'Stocks_data.csv')
    reader = DataReader(data_path)
    data = reader.read()
    # Perform additional assertions on the CSV data if needed

# Run the tests directly (example)
if __name__ == '__main__':
    test_data_reader_integration()