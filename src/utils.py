import os
import sys
import numpy as np
import pandas as pd
#import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging

import requests
from urllib.request import urlretrieve

## utils - Have all the necessary classes and functions that help
### Create the following functions: Save and Load object, Evaluate models

def save_object(file_path:str, obj:object):
    """
    Saves the object in a pickle file

    Args
      file_path:str - Object file path
      obj - Object to save
    
    Returns
      Saves the object in a pickle file
    
    from src.utils import save_object
    save_object(file_path=, obj=)
    """
    try:
        #pass
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path,'wb') as file_obj:
            pickle.dump(obj, file_obj)
    
    except Exception as e:
        raise CustomException(e, sys)
    

#def load_object(file_path:str)-> object:
def load_object(file_path:str):
    """
    Loads the object from a pickle file

    Args
      file_path:str - Object file path
    
    Returns
      Object
    
    from src.utils import load_object
    load_object(file_path=)
    """
    try:
        #pass
        with open(file_path, 'r') as file_obj:
            return pickle.load(file_obj)
    
    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, X_test, y_train, y_test, models, param):
    """
    Trains the models using hyperparameter tuning
    Evaluates the models using specific metrics
    Selects the best performing model

    Args
      file_path:str - Object file path
    
    Returns
      Report
    
    from src.utils import evaluate_models
    evaluate_models(X_train=, X_test=, y_train=, y_test=, models=, param=)
    """
    try:
        pass
    
    except Exception as e:
        raise CustomException(e, sys)
    

def download_data_github(url:str,path_to_save:str, filename_tosave:str):
    """
    ```
    def download_data_github(url:str,path_to_save:str,is_repo_private:bool=False):
    If repository is private need to add
    import requests
    from requests.structures import CaseInsensitiveDict
    headers = CaseInsensitiveDict()
    headers['Authorization'] = "Add private token here"
    resp = requests.get(url, headers=headers)
    print(resp.status_code)
    ```

    from src.utils import download_data_github
    download_data_github(url=,path_to_save=)
    """
    try:
        #pass
        ## Create directories if they do not exist
        #logging.info(f"src/utils/download_data_github")
        if not os.path.exists(path_to_save):
        #if not os.path.isdir(path_to_save):
            os.makedirs(path_to_save, exist_ok=True)
        
        ### Get content from website and save it
        resp = requests.get(url)
        with open(os.path.join(path_to_save,filename_tosave), 'wb') as file:
            print("Writing contents in file")
            file.write(resp.content)
        #logging.info(f"Downloaded data from Github successfully")

    except Exception as e:
        raise CustomException(e, sys)