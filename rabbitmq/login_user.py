import getpass

def login_user(result):
	ipadr = input(f'Enter new IP for RMQ Cluster or use this {result}: ') or result
	user = input('Enter username for RMQ: ')
	passwd = getpass.getpass('Enter password for RMQ: ')
	return user, passwd, ipadr