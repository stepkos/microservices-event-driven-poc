__all__ = ["logger"]

import sys
import logging

from config.constants import LOGGER_FORMAT, LOGGER_DATE_FORMAT


def configure_logger() -> logging.Logger:

    formatter = logging.Formatter(LOGGER_FORMAT, LOGGER_DATE_FORMAT)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.INFO)
    stdout_handler.setFormatter(formatter)

    logger_ = logging.getLogger(__name__)
    logger_.setLevel(logging.INFO)
    logger_.addHandler(stdout_handler)

    return logger_


logger = configure_logger()
