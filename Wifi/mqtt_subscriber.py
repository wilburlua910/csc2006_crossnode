import paho.mqtt.client as mqtt
import json
import time
import datetime

def on_message(client, userdata, message):

    #Conver the data from Byte/Byte Array into json string
    json_string_data = str(message.payload.decode("utf-8"))

    json_data = json.loads(json_string_data)
    timestamp = datetime.datetime.fromtimestamp(float(json_data['timestamp']))
    print("Vehicle straight : ", json_data['vehicles_straight'])
    print("Vehicle right : ", json_data['vehicles_right'])
    
    print("timestamp: ", timestamp)
    
#Master Controller to subscribe to the topic, run the algorithm and change LED matrix
broker_address="172.20.10.4"
client = mqtt.Client("Master controller")
client.on_message = on_message
client.connect(broker_address)
client.subscribe("Traffic/Edge1")

client.loop_forever()


