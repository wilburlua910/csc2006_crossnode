# Smart Traffic Junction Project

## WiFi -MQTT
- pip install ``` pip install mosquitto ```
- reconfigure a new config file in ``` /etc/mosquitto/ ```
- enable the new config file to not listn to Local Only
- To run the broker, stop the current Mosquitto service on the pi: ``` sudo systemctl stop mosquitto ```
- Run the verbose on the new config file: ``` sudo mosquitto -c newconfig.conf -p 1883 -v ```
- Pi is now a broker and the controllers and other pi devices can now connect to it
