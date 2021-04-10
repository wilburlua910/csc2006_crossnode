from bluepy import btle
import time

SYSTEM_TIME = time.time()

def writeTxt(inputTime):
    time = str(inputTime) + "\r\n"
    f = open("Controller_Bluetooth.txt", "a")
    f.write(time)
    f.close()

def getCurrentTime(input):
    timenow = str(round((time.time()-SYSTEM_TIME)*1000)) + " ms"
    writeTxt(timenow)


print("Connecting...")
dev = btle.Peripheral("b8:27:eb:82:de:18")
time.sleep(1)
dev.setMTU(40)

print("Services...")
for svc in dev.services:
    for char in svc.getCharacteristics():
        getCurrentTime(print(char.read()))
        