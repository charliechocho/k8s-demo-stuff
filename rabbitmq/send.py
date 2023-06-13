#!/usr/local/bin/ python3

from app_tasks import check_ip, check_user, login_user 
import pika
from faker import Faker

fake = Faker()
cont = 'y'

def create_msg(user, passwd, ipadr, cont = 'y', names = []):
	while cont == 'y':
		credentials = pika.PlainCredentials(user, passwd)
		parameters = pika.ConnectionParameters(ipadr,
										5672,
										'/',
										credentials)

		
		try:
			connection = pika.BlockingConnection(parameters)
			channel = connection.channel()
		except pika.exceptions.ProbableAuthenticationError:
			print(
			'''
			It seems you might have entered the wrong user or password!
			Make sure you have the right credentials and try again!
			'''
				)
			exit()

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

result = check_ip()
user, passwd, ipadr = login_user(str(result))
check_user(user, passwd)
create_msg(user, passwd, ipadr)

