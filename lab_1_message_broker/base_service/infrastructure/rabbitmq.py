import ssl
from contextlib import contextmanager

import certifi
import pika

from config import logger
from config.constants import (
    RABBITMQ_HOST,
    RABBITMQ_PASSWORD,
    RABBITMQ_PORT,
    RABBITMQ_PORT_SSL,
    RABBITMQ_USER,
)


def get_pika_parameters() -> pika.ConnectionParameters:
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
    parameters = pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        port=RABBITMQ_PORT,
        credentials=credentials,
    )
    return parameters


def get_pika_parameters_ssl() -> pika.ConnectionParameters:
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    ssl_options = pika.SSLOptions(ssl_context)
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
    parameters = pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        virtual_host=RABBITMQ_USER,
        port=RABBITMQ_PORT_SSL,
        credentials=credentials,
        ssl_options=ssl_options,
    )
    return parameters


class RabbitMQClient:
    def __init__(
        self,
        parameters: pika.ConnectionParameters = None,
        auto_connect: bool = True,
    ):
        self.parameters = parameters or get_pika_parameters()
        self.connection: pika.BlockingConnection | None = None
        self.channel: pika.adapters.blocking_connection.BlockingChannel | None = None
        if auto_connect:
            self.connect()

    def connect(self):
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()

    def close(self):
        if not self.connection or not self.channel:
            logger.info("Connection and channel are already closed.")
            return

        if self.channel.is_open:
            self.channel.close()
        if self.connection.is_open:
            self.connection.close()
        logger.info("Connection and channel closed.")

    @classmethod
    @contextmanager
    def ctx(cls, parameters: pika.ConnectionParameters = None):
        client = cls(parameters=parameters)
        try:
            yield client
        finally:
            client.close()

    def queue_declare(
        self,
        queue_name: str,
        durable: bool = True,
        prefetch_count: int | None = 1
    ):
        self.channel.queue_declare(queue=queue_name, durable=durable)
        if prefetch_count is not None:
            self.channel.basic_qos(prefetch_count=prefetch_count)
        logger.info(f"Declared queue {queue_name}")

    def publish(self, event_name, message, persistent: bool = True):
        self.channel.basic_publish(
            exchange="",
            routing_key=event_name,
            body=message,
            properties=(
                pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent)
                if persistent
                else None
            ),
        )
        logger.info(f"Published {event_name}: {message}")

    def consume(
        self,
        event_name: str,
        callback,
        auto_ack: bool = False,
    ):
        self.channel.basic_consume(
            queue=event_name, on_message_callback=callback, auto_ack=auto_ack
        )
        logger.info(f"Subscribed to {event_name}")
        self.channel.start_consuming()
