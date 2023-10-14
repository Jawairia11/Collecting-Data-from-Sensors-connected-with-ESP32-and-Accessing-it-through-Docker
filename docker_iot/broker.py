import random, time
import paho.mqtt.client as mqtt
import json
 
broker_address = "192.168.32.1" 
# broker_address = "example.com" 
client = mqtt.Client("Publisher")
client.connect(broker_address)


while (True):
#   msg = {f"temprature":random.randint(0,10)}
    msg = {
       "sensor": {
          "dht22": {
             "temperature": random.random()*100,
             "moisture": random.random()*100
          },
          "ultrasonic": {
             "distance": random.random()*100
          }
       }
    }
    
    msg_json = json.dumps(msg)
    time.sleep(1)
    client.publish("sensor/temperature", msg_json)
    print(msg_json)