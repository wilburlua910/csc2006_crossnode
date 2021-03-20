from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo
import logging
import time

#ThingsBoard IP 
THINGSBOARD_HOST = '129.126.163.157'

#Access token of Controller
ACCESS_TOKEN = 'M5enL3ND6Jl9KX1mRwje'

INTERVAL=2



#Controller device
client = TBDeviceMqttClient(THINGSBOARD_HOST, ACCESS_TOKEN)

#Call back 
def on_attribute_change(client,result, exception):
    print(client)

    # get client key & values and print it 
    # junction1_result will be the value
    clientObj = result["client"]
    junction1_result = clientObj["junction1"]
    print(junction1_result)
    if exception is not None:
        print("Exception: " + str(exception))
    else:
        print(result)
        

client.connect()
#client.request_attributes(["junction1", "junction2"], callback=on_attribute_change)

#Poll for changes
while True:
    client.request_attributes(["Edge1_Len", "Edge1_Straight", "Edge1_Right", "Edge2_Len", "Edge2_Straight", "Edge2_Right"],callback=on_attribute_change)  
    time.sleep(5)



