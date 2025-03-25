import os
from datetime import datetime
import logging

## datetime.now() month_day_year_hour_minute_seconds
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

##Do it in CWD 'cwd/logs/month_day_year_hour_minute_seconds'
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

##
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)s %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)