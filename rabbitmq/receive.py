#!/usr/local/bin/ python3

import pika, sys, os

credentials = pika.PlainCredentials('msoderberg', 'VMware1!')
parameters = pika.ConnectionParameters('10.220.3.41',
                                   5672,
                                   '/',
                                   credentials)

def main():
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='hello Tanzu')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue='hello Tanzu', auto_ack=True, on_message_callback=callback)

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
