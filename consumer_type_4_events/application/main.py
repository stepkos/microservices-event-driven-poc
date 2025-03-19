import time

from domain.events import BaseEvent, Type4Event
from infrastructure.rabbitmq import RabbitMQClient
from config import logger

event_classes = BaseEvent.__subclasses__()


def callback(ch, method, properties, body):
    body = body.decode()
    logger.info(f"Consuming message: {body}")
    time.sleep(2)
    logger.info(f"Done consuming message: {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def consume_events():
    with RabbitMQClient.ctx() as client:
        for event_class in event_classes:
            client.queue_declare(event_class.get_event_name())

        client.consume(Type4Event.get_event_name(), callback)


consume_events()
