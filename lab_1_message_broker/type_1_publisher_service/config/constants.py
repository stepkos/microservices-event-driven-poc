import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

MAIN_FOLDER_NAME = Path(__file__).parents[1].name

LOGGER_FORMAT = f'%(asctime)s {MAIN_FOLDER_NAME}: %(message)s'
LOGGER_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT')
RABBITMQ_USER = os.getenv('RABBITMQ_USER')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD')
