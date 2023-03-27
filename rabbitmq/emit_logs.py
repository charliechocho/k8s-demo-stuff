#!/usr/bin/env python

import pika
import sys

credentials = pika.PlainCredentials('msoderberg', 'VMware1!')
parameters = pika.ConnectionParameters('10.220.40.70',
                                   5672,
                                   '/',
                                   credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

message = ''.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='severity', body=message)
print(f" [x] Sent {message}")

connection.close()