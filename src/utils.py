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