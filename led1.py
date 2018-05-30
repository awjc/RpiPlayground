import RPi.GPIO as GPIO

import time
from output_pin import OutputPin
from input_pin import InputPin

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

button = InputPin(17, True)
led = OutputPin(21, False, True)

status = True
while True:
    button.wait_for_edge(GPIO.BOTH, 50)
    led.set_status(False if button.read() else True)
    
