#!/usr/local/bin/ python3

import os 
import json
import getpass 
import pika
from faker import Faker

fake = Faker()
cont = 'y'

def check_ip():
	if os.path.isfile('config.json'):
		with open('config.json', 'r') as f:
			conf = json.load(f)
			return conf['ipadr']
	else:
		ipadr = input('Enter the ipadress to the RMQ cluster: ')
		if ipadr:
			conf = {"ipadr":ipadr}
			with open('config.json', 'w') as f:
				json.dump(conf, f, indent = 4, sort_keys = True)
				return ipadr
		else:
			print('seems You did not enter a valid IP')
			exit()



def login_user(result):
	ipadr = input(f'Enter new IP for RMQ Cluster or use this {result}: ') or result
	user = input('Enter username for RMQ: ')
	passwd = getpass.getpass('Enter password for RMQ: ')
	return user, passwd, ipadr

def check_user(user, passwd):
	if user and passwd:
		names = []
		return names
	else:
		print('User and/or Password not entered\nExiting App!')
		exit()

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

