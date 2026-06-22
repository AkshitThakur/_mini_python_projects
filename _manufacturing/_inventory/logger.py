import config, logging, colorlog

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

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
file_handler = logging.FileHandler(config.LOG_FILE)
file_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s | %(levelname)s | %(funcName)s | %(message)s"
    )
)
logger.addHandler(file_handler)