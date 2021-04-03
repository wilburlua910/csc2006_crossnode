import paho.mqtt.client as mqtt
import time

# CALLBACK FUNCTIONS
def on_log(client, userdata, level, buf):
    print("log: "+buf)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected result code "+str(rc))

def on_message(client,userdata,msg):
    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8", "ignore"))
    print("Message received",m_decode)
    print("Topic: "+str(topic))

# Set up CONNECTION VARIABLES
# Set IP address of broker
# broker = "localhost"
# broker = "test.mosquitto.org"
port = 1883
broker="169.254.238.24"
# broker="pi.local"

# Name the client within the arguement
client = mqtt.Client("Zy")

# Binding all callback functions
client.on_connect=on_connect
client.on_disconnect=on_disconnect
client.on_log=on_log
client.on_message=on_message

# Setting up connection to the broker
print("Connecting to broker: ",broker)
client.connect(broker,port)

# Loop needed for callback to work
client.loop_start()


# SUBSCRIBE CODE
client.subscribe("smell123")

while(True):
# PUBLISH CODE 
# ARGS:(topic, message)
    time.sleep(4)



client.loop_stop
client.disconnect()