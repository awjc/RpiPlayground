import RPi.GPIO as GPIO

import time
from output_pin import OutputPin
from input_pin import InputPin

print('Initializing...')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = InputPin(17)
led = OutputPin(4, False)

print('Ready.')
status = True
while True:
    button.wait_for_edge(GPIO.BOTH, 50)
    led.set_status(False if button.read() else True)
    
