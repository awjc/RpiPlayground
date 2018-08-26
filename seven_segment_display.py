import RPi.GPIO as GPIO

import time
from math import sqrt; from itertools import count, islice

from output_pin import OutputPin
from input_pin import InputPin

print('Initializing...')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

""" The ports for the SSD, in order of pin connection on the board.
    There is one port per segment, and one for the dot, for a total of 8.
"""
ports = [26, 19, 6, 5, 21, 20, 12, 25]

""" These ports seem to cause the SSD to just go dark when the pins are high,
    no matter what the other pins are. We just make sure they get set to low
    on init and don't get touched after that.
"""
bad_ports = [13, 16]

zero  = [0, 1, 1, 1, 1, 1, 1, 0]
one   = [0, 0, 0, 1, 0, 0, 1, 0]
two   = [1, 0, 1, 1, 1, 1, 0, 0]
three = [1, 0, 1, 1, 0, 1, 1, 0]
four  = [1, 1, 0, 1, 0, 0, 1, 0]
five  = [1, 1, 1, 0, 0, 1, 1, 0]
six   = [1, 1, 1, 0, 1, 1, 1, 0]
seven = [0, 0, 1, 1, 0, 0, 1, 0]
eight = [1, 1, 1, 1, 1, 1, 1, 0]
nine  = [1, 1, 1, 1, 0, 1, 1, 0]
digits = [zero, one, two, three, four, five, six, seven, eight, nine]

button = InputPin(17)
led = OutputPin(4, False)

for port in ports:
    GPIO.setup(port, GPIO.OUT)
for bad_port in bad_ports:
    GPIO.setup(bad_port, GPIO.OUT)
    GPIO.output(bad_port, GPIO.LOW)

def print_num(number_array):
    for idx in range(len(ports)):
        bins = [True if int(i) else False for i in number_array]
        GPIO.output(ports[idx], GPIO.HIGH if bins[idx] else GPIO.LOW)

def is_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))


counter = 0
print_num(zero)
while True:
    button.wait_for_edge(GPIO.FALLING, bouncetime=300)
    print_num(digits[counter])
    led.set_status(is_prime(counter))
    counter = (counter + 1) % 10
        
        
        
    
