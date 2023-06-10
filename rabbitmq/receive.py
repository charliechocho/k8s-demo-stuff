#!/usr/local/bin/ python3

import getpass
import pika, sys, os

user = input('Enter username for RMQ: ')
passwd = getpass.getpass('Enter password for RMQ: ')

if not user and passwd:
	print('User and/or Password not entered\nExiting App!')
	exit()
        
credentials = pika.PlainCredentials(user, passwd)
parameters = pika.ConnectionParameters('10.220.74.7',
                                   5672,
                                   '/',
                                   credentials)

def main():
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='Tanzu Cities')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue='Tanzu Cities', auto_ack=True, on_message_callback=callback)

    print(' [*] Waiting for messages! To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
