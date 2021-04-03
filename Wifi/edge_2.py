import paho.mqtt.client as mqtt #import the client1
import time
import json
############

SYSTEM_TIME =time.time()
global data

def getCurrentTime(input):
    timenow = round((time.time()-SYSTEM_TIME)*1000)
    return timenow
    #print("Queue is:", data["Queue"])
    #print("\n\n message topic=",message.topic)
    # print("\n\n message qos=",message.qos)
    # print("\n\n message retain flag=",message.retain)
    # print("\n\n Time sent: ", (round((time.time()-SYSTEM_TIME)*1000)-4000), " ms")
########################################

broker_address="172.20.10.4"
print("creating new instance")
client = mqtt.Client("Edge_2") #create new instance
print("connecting to broker")
client.connect(broker_address) #connect to broker

i=0
client.loop_stop
client.loop_start() #start the loop
while(True):
    i += 1
    time.sleep(5)
    
    print("Publishing message to topic","Traffic/Edge1")
    data = {
        "vehicles_straight" : 4,
        "vehicles_right": 10,
        "timestamp": str(time.time())

    }
    msg = json.dumps(data)
    print(type(data))
    print(type(msg))
    #msg_to_json = json.dumps(MSG)
    client.publish("Traffic/Edge1", msg)

    #print("Time: ",(getCurrentTime(client.publish("Traffic/Edge1","4"))-(1000*i)), " ms")
# time.sleep(20) # wait
client.loop_stop() #stop the loop