import paho.mqtt.client as mqtt #import the client1
import time
import json
import random
############

SYSTEM_TIME =time.time()
global data


    #print("Queue is:", data["Queue"])
    #print("\n\n message topic=",message.topic)
    # print("\n\n message qos=",message.qos)
    # print("\n\n message retain flag=",message.retain)
    # print("\n\n Time sent: ", (round((time.time()-SYSTEM_TIME)*1000)-4000), " ms")
########################################

def writeTxt(inputTime):
    f = open("Timing.txt", "w+")
    f.write(inputTime, "\r\n")
    f.close()

def getCurrentTime(input, i):
    timenow = (round((time.time()-SYSTEM_TIME)*1000)-(5000*i))
    writeTxt(timenow)
    return timenow

# def writeTxt(output):
#     f = open("Timing.txt", "w+")

#     for i in range:
#         f.write("Time: ", i, " - ", output, " \r\n")
    
#     f.close()


broker_address="172.20.10.4"
print("creating new instance")
client = mqtt.Client("Edge_1") 
print("connecting to broker")
client.connect(broker_address)

i=0
client.loop_stop
client.loop_start() #start the loop
while(True):
    i += 1
    time.sleep(5)
    lane_data = {
        "straight": 5,
        "right": 2 
    }
    print("Publishing message to topic","Traffic/Edge1")
    data = {
        "section": 1,
        "lane": lane_data,
        "timestamp": str(time.time())
    }
    msg = json.dumps(data)
    print(type(data))
    print(type(msg))
    #msg_to_json = json.dumps(MSG)
    print(getCurrentTime(client.publish("Traffic/Edge1", msg, qos=0, retain=False), i), " ms (Edge1)")
    #print("Time: ",(getCurrentTime(client.publish("Traffic/Edge1","4"))-(1000*i)), " ms")
# time.sleep(20) # wait
client.loop_stop() #stop the loop