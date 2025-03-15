import time
import random

from domain.events import Type2Event
from infrastructure.rabbitmq import RabbitMQClient


def publish_events():
    with RabbitMQClient.ctx() as client:
        while True:
            event = Type2Event(content="event content")
            client.publish(event.get_event_name(), event.content)
            time.sleep(random.random() * 10)


publish_events()
