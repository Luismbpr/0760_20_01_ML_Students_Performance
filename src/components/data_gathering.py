import os
import sys
from pathlib import Path
import requests
from zipfile import ZipFile
from dotenv import load_dotenv
load_dotenv()

from src.logger import logging
from src.exception import CustomException
from src.utils import download_data_github

#print(f"GITHUB_USERNAME:\n{os.getenv("GITHUB_USERNAME")}")

#getmddd = os.path.join(os.getenv('GITHUB_USERNAME'),os.getenv('GITHUB_USERNAME002'))
#print(getmddd)## Returns: Luismbpr/JOHNDOE

dataset_url= "https://raw.githubusercontent.com/Luismbpr/datasets_001/refs/heads/main/datasets/students_performance_0760.csv"


file_name='students_performance_0760.csv'
#path_to_save='/Users/luis/Documents/Programming/dev/0760 Complete MLOps Bootcamp With 10 Plus End To End ML Projects Krish Naik/venv_0760_Complete_MLOps_Bootcamp_Krish_Naik_312_01/0760_Course/Section 20 End To End DS Project implementation With Mulitple AWS, Azure Deployment/venv_0760_20_01_312_001/0760_20_01_ML_Students_Performance/notebooks/data/'

path_to_save_nofilename= os.path.join(os.getcwd(), 'notebooks','data')


#path_to_save_wfilename = os.path.join(os.getcwd(),'notebooks','data', file_name)
#print(f"path_to_save:\n{path_to_save_wfilename}")

try:
    #logging.info(f"data_gathering: Trying to gather and download file: {file_name} from GitHub.")
    download_data_github(url=dataset_url,path_to_save=path_to_save_nofilename, filename_tosave=file_name)
    #logging.info(f"data_gathering: successfully downloaded data from GitHub.")
except Exception as e:
    raise CustomException(e, sys)



#timeout = 10
#url = os.getenv("ORIGINAL_DATA_PATH_ONLINE")
#r = requests.get(url=url, timeout=timeout)
#try:
#    if r.ok:
#        print(f"File found: {r.content}")
#        with ZipFile(r.content) as f:
#            for file in f.namelist():
#                if file.endswith(file_name):
#                    print(f"File found: {r.content}")
#                    data = f.read(f)

#    else:
#        pass
#except Exception as e:
#    raise CustomException(e, sys)