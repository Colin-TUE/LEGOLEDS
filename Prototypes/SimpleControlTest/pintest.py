from machine import Pin
import time

def pintest(pinNr):
    # create an output pin on pin #0
    p0 = Pin(pinNr, Pin.OUT)

    # set the value low then high
    print("pins on")
    p0.value(1)
    time.sleep(10)
    print("pins off")
    p0.value(0)

pintest(21)