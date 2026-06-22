# Discount Calculator
import json

import logging
import colorlog
from pathlib import Path
DIR = Path("_ecommerce")
FILE_NAME = DIR / "_discount.json"
LOG_FILE = DIR / "_discount.log"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Console Handler (Colored)
console_handler = colorlog.StreamHandler()
console_handler.setFormatter(
    colorlog.ColoredFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s | %(blue)s%(funcName)s%(reset)s | %(message)s",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
    )
)
logger.addHandler(console_handler)
# File Handler (No Colors)
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s | %(levelname)s | %(funcName)s | %(message)s"
    )
)
logger.addHandler(file_handler)

