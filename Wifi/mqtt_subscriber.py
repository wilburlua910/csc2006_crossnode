import paho.mqtt.client as mqtt
import json
import time
import datetime



SYSTEM_TIME = time.time()
class junction:

    def __init__(self):
        self.junctionData = []
        
        #Flags
        self.section1 = False
        self.section2 = False

    def algo(self, list):
        print("Algo ")
        
    # def sort(self, data):

def writeTxt(inputTime):
    time = str(inputTime) + " \r\n"
    f = open("Controller_Wifi.txt", "a")
    f.write(time)
    f.close()

def getCurrentTime():
    
    timenow = (round((time.time()-SYSTEM_TIME)* 1000))
    writeTxt(timenow)
    return timenow
    

def on_message(client, userdata, message):
    getCurrentTime()
    #Passing object to the calback
    junction_obj = userdata['junction']
    #Conver the data from Byte/Byte Array into json string
    json_string_data = str(message.payload.decode("utf-8"))
    json_data = json.loads(json_string_data)
    
    
    #Check from which section
    section = json_data['section']
    lane = json_data['lane']

    if section == 1 and junction_obj.section1 is False:
        print("Section 1 arrived...")

        junction_obj.section1 = True
        data = {
        "section" : section,
        "lane": lane
        }
        junction_obj.junctionData.append(data)

    elif section == 2 and junction_obj:
        print("Section 2 arrived...")

        junction_obj.section2 = True
        data = {
        "section" : section,
        "lane": lane
        }
        junction_obj.junctionData.append(data)
    else:
        pass

    if (junction_obj.section1 and junction_obj.section2 is True):
        print("Both data arrived", junction_obj.junctionData)

        list1 = junction_obj.junctionData
        junction_obj.algo(list1)
        junction_obj.junctionData = []
        junction_obj.section1, junction_obj.section2 = False, False
        

        #Call the algo
    
#Master Controller to subscribe to the topic, run the algorithm and change LED matrix
broker_address="172.20.10.4"
junction_obj = junction()
data = {
    "junction": junction_obj
}

client = mqtt.Client("Master controller", userdata=data)
client.on_message = on_message
client.connect(broker_address)
print(client.subscribe("Traffic/Edge1",qos=1))
#client.subscribe("Traffic/Edge2", qos=0)
client.loop_forever()


