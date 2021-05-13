import pika, json

params = pika.URLParameters('amqps://leafhtmg:1zdyVnp9-0baSYZHK6Hhxjutin_rawGw@dove.rmq.cloudamqp.com/leafhtmg')
connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)