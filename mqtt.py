#my code
from flask import Flask, request
import threading 
import paho.mqtt.client as mqtt
import requests
import json

import os

response = ""
######added now........unique = ['1','mars', 'elvis', 'Kori', 'brian','205', 'keith']    
data = {}

def start_mqtt_subscriber():
    #####i doubt whether this 2 lines of code are functional
    clientid="14"
    client = mqtt.Client(client_id=clientid)

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            # data = request.get_json()
        # Perform an HTTP request
            # url = data.get('url')
            # response = requests.get(url)
            client.subscribe("NO2",0)  # Subscribe to all topics under the client's ID
            
            
            print("Connected to MQTT broker")
            
        else:
            print(f"Connection failed with code {rc}")
    
    def on_message(client, userdata, message):
        
        topic = message.topic
        answer = message.payload.decode()
        #payload = message.payload.decode()
        print(f"Received message on topic: {topic}, payload: {answer}")
        if topic == "NO2":
            data["NO2"]=answer
            print(answer)
            if answer == "5":       
        
            
            # Process the incoming MQTT message here above
                url = 'http://localhost:5000/call'
                # payload = {'temp': 10}
                #data = {'data': 'hey george'}
                r = requests.post(url, data=data)
                print(data)
                print(r.text)
        
        
    client.on_connect = on_connect
    client.on_message = on_message
    broker_address = "mqtt.eclipseprojects.io"  # Replace with your broker's address
    client.connect(broker_address, 1883, 30)
    
    
    
    
    # Start the MQTT subscriber loop
    client.loop_forever()

if __name__ == '__main__':
    start_mqtt_subscriber()



