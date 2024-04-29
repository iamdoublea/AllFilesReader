import os
from pathlib import Path

package_name = "all_files_reader"

files_to_create = [
".github/workflow/ci.yaml",
"src/__init__.py",
f"src/{package_name}/__init__.py",
f"src/{package_name}/filereader_crud.py",
"test/__init__.py",
"test/unit/__init__.py",
"test/unit/unit.py",
"test/integration/__init__/py",
"test/integration/int.py",
"init_setup.sh",
"requirements.txt",
"requirements_dev.txt",
"setup.py",
"setup.cfg",
"pyproject.toml",
"tox.ini",
"experiments/experiments.ipynb"
]

for filepath in files_to_create:
    filepath = Path(filepath)
    filedr,filename = os.path.split(filepath)
    if filedr != "":
        os.makedirs(filedr,exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass 
    
