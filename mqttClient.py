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
broker="broker.hivemq.com"

# Name the client within the arguement
client = mqtt.Client("Pa Hoe")
client2 = mqtt.Client("Pa Hoe2")

# Binding all callback functions
client.on_connect=on_connect
client.on_disconnect=on_disconnect
client.on_log=on_log
client.on_message=on_message

client2.on_connect=on_connect
client2.on_disconnect=on_disconnect
client2.on_log=on_log
client2.on_message=on_message

# Setting up connection to the broker
print("Connecting to broker: ",broker)
client.connect(broker)
client2.connect(broker)
# Loop needed for callback to work
client.loop_start()
client2.loop_start()

# SUBSCRIBE CODE
client.subscribe("test123")
client2.subscribe("test123")

# PUBLISH CODE 
# ARGS:(topic, message)
client2.publish("test123", "DATA DATA DATA")

time.sleep(4)
client.loop_stop
client.disconnect()
client2.loop_stop
client2.disconnect()