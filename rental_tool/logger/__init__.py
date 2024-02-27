import logging
import os
from datetime import datetime

# Define the log file name with the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the directory where the log files will be stored
log_dir = 'logs'

# Create the full log path
logs_path = os.path.join(log_dir, LOG_FILE)

# Ensure the log directory exists
os.makedirs(log_dir, exist_ok=True)

# Configure the logging
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
