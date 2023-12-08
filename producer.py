import requests
from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
import time
import json




producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda x: json.dumps(x).encode('utf-8'))
link='https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole/station_information.json'

while True:
    
    result=requests.get(link).json()
    for station in result['data']['stations']:
        station=json.dumps(station)
        producer.send('velib',value=station)
    time.sleep(60)



