#!/usr/local/bin/ python3

import getpass 
import pika
from faker import Faker

user = input('Enter username for RMQ: ')
passwd = getpass.getpass('Enter password for RMQ: ')

if user and passwd:
	names = []
	fake = Faker()
else:
	print('User and/or Password not entered\nExiting App!')
	exit()

cont = 'y'
while cont == 'y':
	credentials = pika.PlainCredentials(user, passwd)
	parameters = pika.ConnectionParameters('10.220.74.10',
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
	cont = input('Send more messages?(y/n) ')
	names = []
