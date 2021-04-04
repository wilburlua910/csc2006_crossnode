import json
# from data import data
import time
import paho.mqtt.client as mqtt #import the client1
import arrow as arrow_shape
from sense_hat import SenseHat

position = 1

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Traffic/Lights")

def on_message(client, userdata, message):

    #Message would be a Lights array

    array_lights = json.loads(message.payload.decode("utf-8"))

    #Depends on which traffic light you are 
    if array_lights[position] == True:
        sense.set_pixels(arrow_shape.arrow_green)

    else:
        sense.set_pixels(arrow_shape.full_red)

    json_string = str(message.payload.decode("utf-8"))
    print(json.loads(json_string))
    print(json_string)
    print("entered message")

broker_address="192.168.1.127"
client = mqtt.Client("Test")
client.connect(broker_address)
client.on_connect = on_connect
client.on_message = on_message
# initLight = [True, False, True, False]
client.loop_start()

