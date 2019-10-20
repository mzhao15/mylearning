
# Kafka producer that reads the input data in a loop in order to simulate real time events
# import os
# import sys
from kafka import KafkaProducer
# from datetime import datetime
# import time

# kafka = KafkaClient("54.67.126.144:9092")
source_file = '/home/ec2-user/000000_0'

def generateData(topic):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092']) #"54.67.126.144:9092"
    msg_cnt = 0
    while True:
        with open(source_file) as f:
            for line in f:
                key = line.split(" ")[0]
                producer.send(topic, key, line.rstrip()) # Asynchronous by default
                msg_cnt += 1 
	        time.sleep(0.1)  # Creating some delay to allow proper rendering of the cab locations on the map
        
        source_file.close()

generateData("CabData")