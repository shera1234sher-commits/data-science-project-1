from src.MyProject.exceptions import CustomException
from src.MyProject.logger import logging
import sys

if __name__ == "__main__":
    logging.info("This is an info message.")
    try:
        1 / 0
    except Exception as e:
        logging.info("custom execption")
        raise CustomException(e, sys)
    