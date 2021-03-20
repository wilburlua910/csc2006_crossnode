from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo
import logging
import time

#ThingsBoard IP
THINGSBOARD_HOST = '129.126.163.157'

#Access token of Controller
ACCESS_TOKEN = 'M5enL3ND6Jl9KX1mRwje'

INTERVAL=2

#Access token of edge device 1
ACCESS_TOKEN_EDGE_1 = 'CnpDrS1iinb5fZ4dQD90'


#Sample
sensor_data = {'temperature': 1414114, 'humidity': 0}

#Controller device
client = TBDeviceMqttClient(THINGSBOARD_HOST, ACCESS_TOKEN)
client_to_edge = TBDeviceMqttClient(THINGSBOARD_HOST, ACCESS_TOKEN_EDGE_1)
client.connect()
client_to_edge.connect()

# Sending to attribute and checking the delivery status (QoS = 1 by default)
result = client.send_attributes({"Edge1_Len": 10, "Edge1_Straight": 7, "Edge1_Right": 3})

# send to edge attribute
result2 = client_to_edge.send_attributes({"Edge1_Len": 10, "Edge1_Straight": 7, "Edge1_Right": 3})

success = result.get() == TBPublishInfo.TB_ERR_SUCCESS

success2 = result2.get()==TBPublishInfo.TB_ERR_SUCCESS

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    print("Connected")

    #client.subscribe("tb/crossnode/temperature")

def on_connect2(client_to_edge, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    print("Connected")


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_message2(client_to_edge, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_publish(client, userdata, result):
    print("Data is Published \n",)
    pass
def on_publis2h(client_to_edge, userdata, result):
    print("Data is Published \n",)
    pass
#client.connect(broker_address, 1883, 60)

# while True:
#     client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
#     time.sleep(2)
#     client.loop()

# write method here to compute payload result
# algo here



