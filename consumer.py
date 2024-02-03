
from kafka import KafkaConsumer

consumer = KafkaConsumer('velib-projet-final-data', bootstrap_servers='localhost:9092')

for message in consumer:
    print(message.value)