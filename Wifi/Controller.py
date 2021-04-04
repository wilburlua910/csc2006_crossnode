import json
# from data import data
import time
import paho.mqtt.client as mqtt #import the client1


# Global variables
currentIteration = 0
emptyCount = 0
currentSection = 0

straightGreenLight = [False, False, False, False]
# rightGreenLight: [False, False, False, False]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Traffic/Controller")

def on_message(client, userdata, message):
    json_string = str(message.payload.decode("utf-8"))
    print(json.loads(json_string))
    print(json_string)
    print("entered message")
    #Passing object to the calback
    # junction_obj = userdata['junction']
    #Conver the data from Byte/Byte Array into json string
    # json_string_data = str(message.payload.decode("utf-8"))
    # json_data = json.loads(json_string_data)
    # print(json_data)

def run_algo(data):
    if currentSection == 1:
        currentSection = 0
    else:
        currentSection += 1
        straightGreenLight[currentSection] = True
        straightGreenLight[currentSection + 2] = True
    #return straightGreenLight

def start_loop():
    t=0
    while t < 60:
        mins, secs = divmod(t, 60)
        
        if int(secs)%15 == 0 and int(secs) != 0:
            client.publish("Traffic/Start", "1", qos=0, retain=False)

        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t += 1
    start_loop()


# If it's at 60 seconds, next section will turn green
broker_address="192.168.1.127"
client = mqtt.Client("Test")
client.connect(broker_address)
client.on_connect = on_connect
client.on_message = on_message
# initLight = [True, False, True, False]
client.loop_start()
start_loop()

    

# if currentIteration == 6:
#     if currentSection == 1:
#         currentSection = 0
#     else:
#         currentSection += 1
#     straightGreenLight[currentSection] = True
#     straightGreenLight[currentSection + 2] = True
#     #return straightGreenLight

# traffic = [
#     {
#         "section": 0,
#         "straight": 0,
#         "right": 0
#     },
#     {
#         "section": 1,
#         "straight": 0,
#         "right": 0
#     },
#     {
#         "section": 2,
#         "straight": 0,
#         "right": 0
#     },
#     {
#         "section": 3,
#         "straight": 0,
#         "right": 0
#     }
# ]

# for iSec, sec in enumerate(data):
#     lanes = sec["lanes"]
#     for lane in lanes:
#         if lane["lane"] == 1:
#             traffic[iSec]["right"] += lane["cars"]
#         else:
#             traffic[iSec]["straight"] += lane["cars"]

# # parsed = json
# print(json.dumps(traffic, indent=4, sort_keys=True))
# print(max(traffic["straight"] for traffic in traffic))

# if emptyCount == 3:
#     if currentSection == 3:
#         currentSection = 0
#     else:
#         currentSection += 1
#     straightGreenLight[currentSection] = True
#     # return straightGreenLight[currentSection]
#     # section = next((x for x in traffic if x["section"] == currentSection), None)


# allStraightEqual = all(obj["straight"] == traffic[0]["straight"] for obj in traffic)
# if allStraightEqual != True:
#     maxStraightVal = max(traffic["straight"] for traffic in traffic)
#     highestObj = next((x for x in traffic if x["straight"] == maxStraightVal), None)
#     print(highestObj)

# allRightEqual = all(obj["right"] == traffic[0]["right"] for obj in traffic)
# if allRightEqual != True:
#     maxRightVal = max(traffic["right"] for traffic in traffic)
#     highestObj = next((x for x in traffic if x["right"] == maxRightVal), None)
#     print(highestObj)