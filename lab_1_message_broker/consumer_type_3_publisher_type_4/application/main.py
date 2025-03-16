import time

from domain.events import BaseEvent, Type3Event, Type4Event
from infrastructure.rabbitmq import RabbitMQClient
from config import logger

event_classes = BaseEvent.__subclasses__()


def callback(ch, method, properties, body):
    body = body.decode()
    logger.info(f"Consuming message: {body}")
    time.sleep(3)
    send_event_4()
    logger.info(f"Done consuming message: {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def send_event_4():
    event = Type4Event(content="event type 4 content")
    with RabbitMQClient.ctx() as client:
        client.queue_declare(event.get_event_name())
        client.publish(event.get_event_name(), event.content)


def consume_events():
    with RabbitMQClient.ctx() as client:
        for event_class in event_classes:
            client.queue_declare(event_class.get_event_name())

        client.consume(Type3Event.get_event_name(), callback)


consume_events()
