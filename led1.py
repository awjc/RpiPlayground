import RPi.GPIO as GPIO
import time

class Port(object):
    """A port for GPIO access - keeps track of its status
        
    Attributes:
        portNum: An int for the GPIO port number for this port
        status: A bool for whether the port is active or not
        debug: A bool for whether debug messages are output
    """
    
    statusToSignal = { False: GPIO.LOW, True: GPIO.HIGH }
    
    def __init__(self, portNum = 21, status = False, debug = False):
        self.portNum = portNum
        self.status = status
        self.debug = debug
        initializeGpioPort(portNum, status)
        
    def initializeGpioPort(portNum, status):
        if not (status == True or status == False):
            raise ValueError('Status needs to be bool')
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(portNum, GPIO.OUT)
        if debug:
            print('GPIO %d initialized' % portNum)
        setStatus(statusToSignal[status])
        
    def toggleState():
        status = not status
        setStatus(status)
        
    def setStatus(status):    
        GPIO.output(portNum, statusToSignal[status])
        if debug:
          print('GPIO %d set to %s' % portNum, 'on' if status else 'off')

        
        

port = 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(port, GPIO.OUT)

for i in range(1, 99999):
  print("LED on")
  GPIO.output(port, GPIO.HIGH)
  time.sleep(.5)
  print("LED off")
  GPIO.output(port, GPIO.LOW)
  time.sleep(.5)
