#!/usr/local/bin/ python3

import pika
from faker import Faker
names = []

fake = Faker()

credentials = pika.PlainCredentials('user', 'password')
parameters = pika.ConnectionParameters('10.220.74.6',
                                   5672,
                                   '/',
                                   credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='Tanzu Cities')

for i in range(10):
	names.append(fake.city())

for fName in names:
	channel.basic_publish(exchange='',
                  routing_key='Tanzu Cities',
                  body=f'{fName}')
	print(f" [x] Sent {fName}!")
connection.close()
