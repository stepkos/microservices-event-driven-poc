import time

from domain.events import BaseEvent, Type1Event
from infrastructure.rabbitmq import RabbitMQClient
from config import logger

event_classes = BaseEvent.__subclasses__()


def callback(ch, method, properties, body):
    body = body.decode()
    logger.info(f"Consuming message: {body}")
    time.sleep(2)
    logger.info(f"Done consuming message: {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def publish_events():
    with RabbitMQClient.ctx() as client:
        for event_class in event_classes:
            event = event_class(content="event content")
            client.queue_declare(event.get_event_name())

        while True:
            event = Type1Event(content="event content")
            client.consume(event.get_event_name(), callback)


publish_events()
