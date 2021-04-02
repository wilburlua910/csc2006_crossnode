#!/usr/bin/python3

"""Copyright (c) 2019, Douglas Otwell
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import dbus
from advertisement import Advertisement
from service import Application, Service, Characteristic, Descriptor
import random
from time import time
GATT_CHRC_IFACE = "org.bluez.GattCharacteristic1"
NOTIFY_TIMEOUT = 5000

#Initialize the class called Lane to track 
class Lane():
    def __init__(self):
        self.straight = 0
        self.right = 0
        self.timestamp = 0

class EdgeAvertisement(Advertisement):
    def __init__(self, index):
        Advertisement.__init__(self, index, "peripheral")
        self.add_local_name("Edge Device IOT")
        self.include_tx_power = True

class EdgeService(Service):
    EDGE_SVC_UUID = "00000001-710e-4a5b-8d75-3e5b444bc3cf"

    def __init__(self, index):

        Service.__init__(self, index, self.EDGE_SVC_UUID, True)
        self.add_characteristic(EdgeCharacteristics(self))

class EdgeCharacteristics(Characteristic):
    EDGE_CHARACTERISTIC_UUID = "00000002-710e-4a5b-8d75-3e5b444bc3cf"

    def __init__(self, service):
        self.notifying = False

        Characteristic.__init__(
                self, self.EDGE_CHARACTERISTIC_UUID,
                ["notify", "read"], service)
        self.add_descriptor(EdgeDescriptor(self))

    def get_vehicles(self): 
        value = []
        currentLaneData = Lane()
        currentLaneData.straight = str(random.randint(1, 5))
        currentLaneData.right = str(random.randint(1, 5))
        currentLaneData.timestamp = str(time())
        
        #vehicles = str(550)
        for c in currentLaneData.straight:
            value.append(dbus.Byte(c.encode()))

        for c in currentLaneData.right:
            value.append(dbus.Byte(c.encode()))

        for c in currentLaneData.timestamp:
            value.append(dbus.Byte(c.encode()))
        return value

    def set_edge_callback(self):
        if self.notifying:
            value = self.get_vehicles()
            self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])
        return self.notifying

    def StartNotify(self):
        if self.notifying:
            return
        self.notifying = True

        value = self.get_vehicles()
        self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])
        self.add_timeout(NOTIFY_TIMEOUT, self.set_edge_callback)

    def StopNotify(self):
        self.notifying = False

    def ReadValue(self, options):
        value = self.get_vehicles()
        return value

class EdgeDescriptor(Descriptor):
    EDGE_DESCRIPTOR_UUID = "2901"
    EDGE_DESCRIPTOR_VALUE = "VEHICLE QUEUE LENGTH"

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, self.EDGE_DESCRIPTOR_UUID,
                ["read"],
                characteristic)

    def ReadValue(self, options):
        value = []
        desc = self.EDGE_DESCRIPTOR_VALUE
        for c in desc:
            value.append(dbus.Byte(c.encode()))
        return value

app = Application()
app.add_service(EdgeService(0))
app.register()

adv = EdgeAvertisement(0)
adv.register()

try:
    app.run()
except KeyboardInterrupt:
    app.quit()