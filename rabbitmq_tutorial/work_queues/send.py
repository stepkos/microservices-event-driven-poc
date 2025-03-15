import sys
import pika

from config.utils import get_pika_parameters

parameters = get_pika_parameters()

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='', routing_key='hello', body=message
)
print(f" [x] Sent {message}")

connection.close()
