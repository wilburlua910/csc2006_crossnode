from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo
import logging
import time

#ThingsBoard IP
THINGSBOARD_HOST = '129.126.163.157'

#Access token of Controller
ACCESS_TOKEN = '2rU2SGnT2A3qqGJ5thpf'

INTERVAL=2
#Sample
sensor_data = {'temperature': 1414114, 'humidity': 0}

#Controller device
client = TBDeviceMqttClient(THINGSBOARD_HOST, ACCESS_TOKEN)
client.connect()
#client.send_attributes({"junction1": 1414, "junction2" : 1414})

# Sending telemetry and checking the delivery status (QoS = 1 by default)
result = client.send_attributes({"junction1": 15, "junction2" :15})

success = result.get() == TBPublishInfo.TB_ERR_SUCCESS

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    print("Connected")

    #client.subscribe("tb/crossnode/temperature")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_publish(client, userdata, result):
    print("Data is Published \n",)
    pass

#client.connect(broker_address, 1883, 60)

# while True:
#     client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
#     time.sleep(2)
#     client.loop()