import os

""" Volume Directory """
# App Data
DATA_DIR = '/app/data'
# App Logs
LOG_FILE = 'app.log'
LOG_DIR = '/app/logs'
LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)
LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
