import time
from uartremote import *
import random
from neopixel import NeoPixel
from machine import Pin

n=12
ur=UartRemote()
np=NeoPixel(Pin(21, Pin.OUT), n)


def startup():
    for i in range(n):
        np[i]=(255, 255, 255)    
        np.write()
        print("next LED on")
        time.sleep(1)
    print("all LEDS on")
    time.sleep(10)
    for i in range(n):
        np[i]=(0, 0, 0)
    np.write()
    print("all LEDS off")

def bounce(r, g, b, wait):
    for i in range(4 * n):
        for j in range(n):
            np[j] = (r, g, b)

        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            index = (n - 1) - (i % n)
            np[index] = (0, 0, 0)

        np.write()
        time.sleep_ms(wait)

startup()

print("start bounce")
bounce(0, 0, 255, 500)
print("end bounce")