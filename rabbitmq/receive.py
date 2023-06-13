#!/usr/local/bin/ python3

from app_tasks import check_ip, check_user, login_user
import pika, sys, os

def connect_rmq(user, passwd, ipadr):        
    credentials = pika.PlainCredentials(user, passwd)
    parameters = pika.ConnectionParameters(ipadr, 5672, '/', credentials)
    return parameters

def main(parameters):
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

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue='Tanzu Cities', auto_ack=True, on_message_callback=callback)

    print(' [*] Waiting for messages! To exit press CTRL+C')
    channel.start_consuming()


result = check_ip()
user, passwd, ipadr = login_user(str(result))
check_user(user, passwd)
parameters = connect_rmq(user, passwd, ipadr)

if __name__ == '__main__':
    try:
        main(parameters)
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
