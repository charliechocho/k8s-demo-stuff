import os
import getpass
import json

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
	if ipadr == result:
		user = input('Enter username for RMQ: ')
		passwd = getpass.getpass('Enter password for RMQ: ')
	else:
		conf = {"ipadr":ipadr}
		with open('config.json', 'w') as f:
			json.dump(conf, f, indent = 4, sort_keys = True)
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