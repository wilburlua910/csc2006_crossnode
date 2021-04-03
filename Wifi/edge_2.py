import paho.mqtt.client as mqtt #import the client1
import time
import json
import random
############

SYSTEM_TIME =time.time()
global data

def writeTxt(inputTime):
    time = str(inputTime) + " \r\n"
    f = open("Edge_2.txt", "a")
    f.write(time)
    f.close()

def getCurrentTime(input, i):

    timenow = (round((time.time()-SYSTEM_TIME)*1000)-(5000*i))
    writeTxt(timenow)
    return timenow
    #print("Queue is:", data["Queue"])
    #print("\n\n message topic=",message.topic)
    # print("\n\n message qos=",message.qos)
    # print("\n\n message retain flag=",message.retain)
    # print("\n\n Time sent: ", (round((time.time()-SYSTEM_TIME)*1000)-4000), " ms")
########################################

broker_address="172.20.10.4"
print("creating new instance")
client = mqtt.Client("Edge_2") 
print("connecting to broker")
client.connect(broker_address)

i=0
client.loop_stop
client.loop_start() #start the loop
while(True):
    i += 1
    time.sleep(5)
    lane_data = {
        "straight": 1,
        "right": 0 
    }
    print("Publishing message to topic","Traffic/Edge2")
    data = {
        "section": 2,
        "lane": lane_data,
        "timestamp": str(time.time())
    }
    msg = json.dumps(data)
    print(type(data))
    print(type(msg))
    #msg_to_json = json.dumps(MSG)
    client.publish("Traffic/Edge2", msg)
    print(getCurrentTime(client.publish("Traffic/Edge2", msg, qos=0, retain=False), i), " ms (Edge2)")
# time.sleep(20) # wait
client.loop_stop() #stop the loop