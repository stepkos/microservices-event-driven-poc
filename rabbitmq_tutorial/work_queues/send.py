import sys
import pika

from rabbitmq_tutorial.config.utils import get_pika_parameters

parameters = get_pika_parameters()

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)  # durable=True means keep queue after RabbitMQ restart

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.DeliveryMode.Persistent
    )
)
print(f" [x] Sent {message}")

connection.close()
