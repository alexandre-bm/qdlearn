import logging
from logging import Logger, Handler, Formatter

import datetime as dt

def _create_logger(filename:str, level=logging.INFO) -> Logger:
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(message)s',
        datefmt= '%d-%m-%y %H:%M:%S'
    )
    logger = logging.getLogger("qdlearn")
    file_handler = _create_handler(filename)
    logger.addHandler(file_handler)
    return logger
    
def _create_handler(filename:str, level=logging.WARNING) -> Handler:
    formatter = _create_handler_formatter()
    file_handler = logging.FileHandler(f"logs/{filename}.log")
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    return file_handler

def _create_handler_formatter() -> Formatter:
    string = "%(asctime)s: %(levelname)s - %(message)s"
    formatter = logging.Formatter(string)
    return formatter
        

def main():
    today = dt.datetime.today()
    filename = f"{today.day:02d}-{today.month:02d}-{today.year}"
    logger = _create_logger(filename)
    return logger

LOGGER = main()        