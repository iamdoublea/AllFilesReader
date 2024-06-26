Sure, here's a concise and informative project description for your Python library:

---

## AllFilesReader

The **AllFilesReader** is a versatile Python library designed to simplify the process of reading various types of files with just one click. Whether you need to read CSV, Excel, JSON, MAT, HDF5, Pickle, or JPG images, this library has got you covered.

### Key Features:

- **Wide File Format Support:** Supports reading CSV, Excel, JSON, MAT, HDF5, Pickle, and JPG images, providing a unified interface for accessing data from different file types.
  
- **Graceful Encoding Handling:** Handles potential encoding issues gracefully, ensuring seamless reading of files with automatic detection of encoding or fallback to a default encoding if necessary.
  
- **Error Handling:** Provides detailed error messages and custom exceptions to help troubleshoot issues encountered during the file reading process.
  
- **Simplified Usage:** Offers a straightforward API, making it easy for developers to integrate file reading functionality into their Python projects with minimal effort.

### Installation:

```bash
pip install AllFilesReader
```

### Usage:

```python
from all_files_reader.filereader import DataReader

# Example usage
reader = DataReader("path/to/your/file.csv")
data = reader.read()
print(data)
```

### Getting Started:

Get started with the **AllFilesReaderPythonLibrary** today and streamline your file reading tasks in Python.


