import json
# from data import data
import time
import paho.mqtt.client as mqtt #import the client1


# Global variables
currentIteration = 0
emptyCount = 0
# global CURRENT_SECTION


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

def run_algo(CURRENT_SECTION):
    straightGreenLight = [False, False, False, False]
    if CURRENT_SECTION == 1:
        CURRENT_SECTION = 0
    else:
        CURRENT_SECTION += 1
    
    straightGreenLight[CURRENT_SECTION] = True
    straightGreenLight[CURRENT_SECTION + 2] = True
    client.publish("Traffic/Lights", json.dumps(straightGreenLight), qos=0, retain=False)
    #return straightGreenLight

def start_program(CURRENT_SECTION):
    t=0
    while t < 10:
        mins, secs = divmod(t, 60)

        if int(secs)%10 == 0 and int(secs) != 0:
            client.publish("Traffic/Controller", "1", qos=0, retain=False)

        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t += 1
    run_algo(CURRENT_SECTION)
    # start_program()


# If it's at 60 seconds, next section will turn green
broker_address="192.168.1.127"
client = mqtt.Client("Controller")
client.connect(broker_address)
client.on_connect = on_connect
client.on_message = on_message
initLight = [True, False, True, False]
client.publish("Traffic/Lights", json.dumps(initLight), qos=0, retain=False)
CURRENT_SECTION = 0
start_program(CURRENT_SECTION)
client.loop_forever()

    

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