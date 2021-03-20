from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo
import logging
import time

#ThingsBoard IP 
THINGSBOARD_HOST = '129.126.163.157'

#Access token of Controller
ACCESS_TOKEN = '2rU2SGnT2A3qqGJ5thpf'

INTERVAL=2

#Sample Data
sensor_data = {'temperature': 1414114, 'humidity': 0}

#Controller device
client = TBDeviceMqttClient(THINGSBOARD_HOST, ACCESS_TOKEN)

#Call back 
def on_attribute_change(client,result, exception):
    print(client)
    if exception is not None:
        print("Exception: " + str(exception))
    else:
        print(result)

client.connect()
#client.request_attributes(["junction1", "junction2"], callback=on_attribute_change)

#Poll for changes
while True:
    client.request_attributes(["junction1", "junction2"], callback=on_attribute_change)
    time.sleep(5)