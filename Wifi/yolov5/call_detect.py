import paho.mqtt.client as mqtt #import the client1
import os

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Traffic/Start")


def on_message(client, userdata, message):
    json_string = str(message.payload.decode("utf-8"))
    if json_string == "1":
        print("entered")
        os.system("python3 detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source data/images/")
    print(json_string)

broker_address="192.168.1.127"
client = mqtt.Client("detect")
client.connect(broker_address)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()