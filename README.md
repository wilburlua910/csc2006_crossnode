# Smart Traffic Junction Project

## WiFi -MQTT
### Install Eclipse Mosquitto MQTT
- `sudo apt-get update`
- `sudo apt-get install mosquitto`
- pip install ``` pip install mosquitto ```
- reconfigure a new config file in ``` /etc/mosquitto/ ```
- enable the new config file to not listn to Local Only
- To run the broker, stop the current Mosquitto service on the pi: ``` sudo systemctl stop mosquitto ```
- Run the verbose on the new config file: ``` sudo mosquitto -c newconfig.conf -p 1883 -v ```
- Pi is now a broker and the controllers and other pi devices can now connect to it

### To simulate the traffic light demonstration
- run ``` Controller.py``` on a separate Pi pointing to the Broker's IP address
- run ``` traffic<1/2/3/4>.py ``` on separate Pis pointing to the Broker's IP address

### To get all the dependencies required for Yolov5 object detection model
- `cd /Wifi/Yolov5` 
- `pip3 install -r requirements.txt` 

What if mosquitto not running?

Option 1 
`ps -ef | grep mosquitto` 
`sudo kill <process number>`
or 
`sudo systemctl stop mosquitto`

## Bluetooth
- `pip3 install bluepy`
- use hciconfig to get the MAC addresses of the peripherals
- change the MAC address target inside the bleClient.py
- run `python3 edge_2.py`
- run `python3 bleclient.py`
