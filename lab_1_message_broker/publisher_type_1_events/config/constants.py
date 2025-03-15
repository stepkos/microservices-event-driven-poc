import os

SERVICE_NAME = "publisher_type_1_events"

LOGGER_FORMAT = f"%(asctime)s {SERVICE_NAME}: %(message)s"
LOGGER_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

RABBITMQ_PORT = os.getenv("RABBITMQ_PORT", 5672)
RABBITMQ_PORT_SSL = os.getenv("RABBITMQ_PORT_SSL", 5671)
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
RABBITMQ_USER = os.getenv("RABBITMQ_USER")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")
