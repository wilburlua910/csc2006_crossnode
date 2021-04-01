import paho.mqtt.client as mqtt #import the client1
import time
############

SYSTEM_TIME =time.time()

def getCurrentTime(input):
    timenow = round((time.time()-SYSTEM_TIME)*1000)
    return timenow

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("\n\n message topic=",message.topic)
    # print("\n\n message qos=",message.qos)
    # print("\n\n message retain flag=",message.retain)
    # print("\n\n Time sent: ", (round((time.time()-SYSTEM_TIME)*1000)-4000), " ms")
########################################

broker_address="172.20.10.6"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("Edge_1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker

print("Subscribing to topic","Traffic/Edge1")
client.subscribe("Traffic/Edge1")
i=0
client.loop_stop
client.loop_start() #start the loop
while(True):
    i += 1
    time.sleep(1)
    
    print("Publishing message to topic","Traffic/Edge1")
    print("Time: ",(getCurrentTime(client.publish("Traffic/Edge1","Queue Length: 4"))-(1000*i)), " ms")
# time.sleep(20) # wait
client.loop_stop() #stop the loop