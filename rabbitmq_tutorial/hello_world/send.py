import pika

from rabbitmq_tutorial.config.utils import get_pika_parameters

parameters = get_pika_parameters()

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(
    exchange='', routing_key='hello', body='Hello World!'
)
print(" [x] Sent 'Hello World!'")

connection.close()
