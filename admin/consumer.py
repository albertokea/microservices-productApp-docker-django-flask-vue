import pika

params = pika.URLParameters('amqps://leafhtmg:1zdyVnp9-0baSYZHK6Hhxjutin_rawGw@dove.rmq.cloudamqp.com/leafhtmg')
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Receiving admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started consuming')
channel.start_consuming()

channel.close()