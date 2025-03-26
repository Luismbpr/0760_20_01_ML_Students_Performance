import os
import sys
from pathlib import Path
import requests
from zipfile import ZipFile
from dotenv import load_dotenv
load_dotenv()
from src.exception import CustomException

#print(f"GITHUB_USERNAME:\n{os.getenv("GITHUB_USERNAME")}")

#getmddd = os.path.join(os.getenv('GITHUB_USERNAME'),os.getenv('GITHUB_USERNAME002'))
#print(getmddd)## Returns: Luismbpr/JOHNDOE

file_name='students_performance_01.csv'
timeout = 10
url = os.getenv("ORIGINAL_DATA_PATH_ONLINE")
r = requests.get(url=url, timeout=timeout)
try:
    if r.ok:
        print(f"File found: {r.content}")
        with ZipFile(r.content) as f:
            for file in f.namelist():
                if file.endswith(file_name):
                    print(f"File found: {r.content}")
                    data = f.read(f)

    else:
        pass
except Exception as e:
    raise CustomException(e, sys)