import ssl
import pika
import certifi
from rabbitmq_tutorial.config.envs import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_USER, RABBITMQ_PASSWORD


def get_pika_parameters() -> pika.ConnectionParameters:
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    ssl_options = pika.SSLOptions(ssl_context)
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
    parameters = pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        virtual_host=RABBITMQ_USER,
        port=RABBITMQ_PORT,
        credentials=credentials,
        ssl_options=ssl_options,
    )
    return parameters
