from enum import Enum
from sense_hat import SenseHat
import itertools
import multiprocessing
from time import sleep

class SenseHatLeds:
    '''
    A class to manipulate the LEDs on the SenseHat
    '''

    class TrafficColors(Enum):
        '''
        A class to enumerate the colors of a traffic light
        '''
        RED = [255, 0, 0]
        GREEN = [0, 255, 0]
        YELLOW = [255, 255, 0]

    def __init__(self):
        self.sense = SenseHat()
        self._thread = None
        self._is_colored = False

    def _set_color(self, color: TrafficColors):
        if self._is_colored:
            self._clear()      

        l = list(itertools.repeat(color.value, 64))
        self.sense.set_pixels(l)
        self._is_colored = True

    def _clear(self):
        try:
            self._thread.terminate()
        except:
            pass

        self.sense.clear()

    def _blink_color(self, color: TrafficColors, frequency: int):
        interval = (1000.0 / frequency / 2) / 1000

        while True:
            self._set_color(color)
            sleep(interval)
            self._clear()
            sleep(interval)

    def solid(self, color: TrafficColors):
        '''
        Sets the LEDs on the SenseHat to a solid color.

        Parameters:
            color (SenseHatLeds.TrafficColors): The color to set to.
        '''
        self._set_color(color)

    def blink(self, color: TrafficColors, frequency: int = 1):
        '''
        Blinks the LEDs on the SenseHat with a color at a specified frequency.

        Parameters:
            color (SenseHatLeds.TrafficColors): The color to blink to.
            frequency (int): The frequency in Hz to blink the LEDs.
        '''
        try:
            self._thread.terminate()
        except:
            pass

        self._thread = multiprocessing.Process(target = self._blink_color, args = (color, frequency,))
        self._thread.start()

print(SenseHatLeds.solid.__doc__)

# ins = SenseHatLeds()
# ins.solid(SenseHatLeds.TrafficColors.GREEN)
# sleep(3.5)
# ins.blink(SenseHatLeds.TrafficColors.GREEN)
# sleep(3.5)
# ins.blink(SenseHatLeds.TrafficColors.YELLOW)
# sleep(3.5)
# ins.blink(SenseHatLeds.TrafficColors.RED)
# sleep(3.5)
# ins.solid(SenseHatLeds.TrafficColors.RED)
# sleep(3.5)
# ins._clear()