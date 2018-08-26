import RPi.GPIO as GPIO

import time
import datetime
from math import sqrt; from itertools import count, islice

from output_pin import OutputPin
from input_pin import InputPin


device_folder = '/sys/bus/w1/devices/28-031572f086ff/'
device_file = device_folder + '/w1_slave'

print('Initializing...')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

#CELSIUS CALCULATION
def read_temp_c():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        print ("Waiting for device to initialize")
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = int(temp_string) / 1000.0 # TEMP_STRING IS THE SENSOR OUTPUT, MAKE SURE IT'S AN INTEGER TO DO THE MATH
        temp_c = str(round(temp_c, 1)) # ROUND THE RESULT TO 1 PLACE AFTER THE DECIMAL, THEN CONVERT IT TO A STRING
        return temp_c

#FAHRENHEIT CALCULATION
def read_temp_f():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        print ("Waiting for device to initialize")
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_f = (int(temp_string) / 1000.0) * 9.0 / 5.0 + 32.0 # TEMP_STRING IS THE SENSOR OUTPUT, MAKE SURE IT'S AN INTEGER TO DO THE MATH
        temp_f = str(round(temp_f, 1)) # ROUND THE RESULT TO 1 PLACE AFTER THE DECIMAL, THEN CONVERT IT TO A STRING
        return temp_f


logfilename = time.strftime("/home/adam/templogs/%Y-%m-%d__%H-%M-%S.log", time.gmtime())
print("Writing log data to the file %s" % logfilename)
try:
    with open(logfilename, "w+") as logfile:
        temps = []
        while True:
            ftemp = read_temp_f()
            temps.append(float(ftemp))
            timestamp = int(time.time())
            logfile.write("%s,%s\n" % (timestamp, ftemp))
            datetime = time.strftime("%H:%M:%S", time.localtime())
            print("%s : %sºF" % (datetime, ftemp))
            # Wait for the next second to happen before proceeding so we don't get 2 readings on the same timestamp
            while int(time.time()) == timestamp:
                time.sleep(0.01)
                pass
            print(i)
except KeyboardInterrupt:
    print("Stopping...")
    pass
    
