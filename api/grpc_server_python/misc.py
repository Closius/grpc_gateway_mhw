import os
from datetime import datetime
import multiprocessing as mp
import threading
import logging
import logging.handlers

import settings


def create_rotating_log():
    def get_log_file():
        if not os.path.exists(settings.LOG_FOLDER):
            os.mkdir(settings.LOG_FOLDER)
        return os.path.join(settings.LOG_FOLDER, settings.LOG_FILENAME)

    logger = logging.getLogger("gRPC-server Log")
    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)
        handler = logging.handlers.RotatingFileHandler(get_log_file(), maxBytes=1024 * 1024 * 300, backupCount=5)
        formatter = logging.Formatter('%(asctime)s|%(process)d|%(thread)d|: %(message)s', "%m-%d-%Y %H:%M:%S")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

create_rotating_log()

def log(msg):
    pid = mp.current_process().pid
    thread_id = threading.current_thread().ident
    if settings.IS_DEBUG:
        print(datetime.now().strftime("%H:%M:%S") + f"|{pid}|{thread_id}|: " + str(msg))
    logger = logging.getLogger("gRPC-server Log")
    logger.info(str(msg))
