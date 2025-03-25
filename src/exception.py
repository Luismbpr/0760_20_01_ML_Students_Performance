import sys
import os
from pathlib import Path
import logger

def error_message_details(error, error_detail:sys):
    """
    Whenever an exception gets raised 
    Args
      error
      error_details: sys
    
    Returns
      Error, line number, error message
    
    error_message_details(error=, error_detail=)
    """
    file_name = exc_tb.tb_frame.f_code.co_filename
    _,_,exc_tb =error_detail.exc_info()
    error_message = f"Error occurred in Python script name [{0}], line number [{1}], error message [{2}]".format(file_name,exc_tb.tb_lineno, str(error))
    
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        """
        from src.exception import CustomException
        CustomException(Exception)
        """
        super.__init__(error_message)
        self.error_message = error_message_details(error=error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message