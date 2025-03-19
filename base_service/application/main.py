import time

from domain.events import BaseEvent, Type1Event
from infrastructure.rabbitmq import RabbitMQClient

event_classes = BaseEvent.__subclasses__()

def publish_events():
    with RabbitMQClient.ctx() as client:
        for event_class in event_classes:
            client.queue_declare(event_class.get_event_name())

        while True:
            event = Type1Event(content="event type 1 content")
            client.publish(event.get_event_name(), event.content)
            time.sleep(5)


publish_events()
