import time
from infrastructure.rabbitmq import RabbitMQClient
from domain.events import Type1Event


def publish_type1_events():
    with RabbitMQClient.ctx() as client:
        while True:
            event = Type1Event(content="event content")
            client.publish(event.get_event_name(), event.content)
            time.sleep(5)


if __name__ == "__main__":
    publish_type1_events()
