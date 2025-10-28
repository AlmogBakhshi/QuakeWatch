import os
import logging
import constants.constants as const

def init_volumes():
    logs()
    data()

def logs():
    os.makedirs(const.LOG_DIR, exist_ok=True)
    logging.basicConfig(filename=const.LOG_PATH, level=logging.WARNING, format=const.LOGGING_FORMAT)

def data():
    os.makedirs(const.DATA_DIR, exist_ok=True)
