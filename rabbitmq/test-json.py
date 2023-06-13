import os
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
		else:
			print('seems You did not enter a valid IP')
			exit()

				
result = check_ip()

if result:
	print(result)
