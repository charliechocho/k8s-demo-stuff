#!/usr/local/bin/ python3

import pika
import sys

credentials = pika.PlainCredentials('msoderberg', 'VMware1!')
parameters = pika.ConnectionParameters('10.220.40.70',
                                   5672,
                                   '/',
                                   credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name, routing_key='black')

print(f" [*] Waiting for logs. To exit press CTRL+C")

def callback(ch, method, properties, body):
    print(f" [x] {body}")

channel.basic_consume(queue=queue_name, 
    on_message_callback=callback, auto_ack=True)

channel.start_consuming()

