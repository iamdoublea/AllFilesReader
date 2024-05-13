#To make sure that the package works well in real world situation, on an overall basis
#To make sure all the components are working well with each other

import os
from src.all_files_reader.filereader_crud import DataReader

def test_data_reader_integration():
    """Tests DataReader with actual file reading (integration test).

    This test assumes sample data files exist in a specific location.
    You may need to adjust paths or create sample files.
    """

    # Test CSV
    data_path = os.path.join('test_data', 'data.csv')
    reader = DataReader(data_path)
    data = reader.read()
    # Perform additional assertions on the CSV data if needed

    # Test image (assuming JPG)
    data_path = os.path.join('test_data', 'image.jpg')
    reader = DataReader(data_path)
    data = reader.read()
    # Perform assertions on image data (e.g., dimensions, format)

    # ... (Add tests for other formats as needed)

# Run the tests directly (example)
if __name__ == '__main__':
    test_data_reader_integration()