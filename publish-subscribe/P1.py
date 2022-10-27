#!/usr/bin/env python
from datetime import datetime
import pika, json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel1 = connection.channel()
channel2 = connection.channel()

channel1.queue_declare(queue='a')
channel2.queue_declare(queue='b')

channel1.basic_publish(exchange='',
    routing_key='a',
    body=json.dumps({'productor': 'P1', 'en': 'Alfa', 'timestamp': datetime.timestamp(datetime.now())}),
    properties=pika.BasicProperties(
        delivery_mode = 2, # make message persistent
    ))

channel2.basic_publish(exchange='',
    routing_key='b',
    body=json.dumps({'productor': 'P1', 'en': 'Beta', 'timestamp': datetime.timestamp(datetime.now())}),
    properties=pika.BasicProperties(
        delivery_mode = 2, # make message persistent
    ))

print(" [x] Sent msgs")
connection.close()