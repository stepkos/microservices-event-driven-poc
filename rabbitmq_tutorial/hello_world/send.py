import ssl
import pika
import certifi
from config.envs import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_USER, RABBITMQ_PASSWORD

ssl_context = ssl.create_default_context(cafile=certifi.where())
ssl_options = pika.SSLOptions(ssl_context)

credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
parameters = pika.ConnectionParameters(
    host=RABBITMQ_HOST,
    virtual_host=RABBITMQ_USER,
    port=RABBITMQ_PORT,
    credentials=credentials,
    ssl_options=ssl_options,
)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(
    exchange='', routing_key='hello', body='Hello World!'
)
print(" [x] Sent 'Hello World!'")

connection.close()
