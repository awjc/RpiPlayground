import RPi.GPIO as GPIO


class OutputPin(object):
    """An output port for GPIO access - keeps track of its status
        
    Attributes:
        port_num: An int for the GPIO port number for this port
        status: A bool for whether the port is active or not
        debug: A bool for whether debug messages are output
    """
    
    status_to_signal = { False: GPIO.LOW, True: GPIO.HIGH }
    
    def __init__(self, port_num, status = False, debug = False):
        self.debug = debug
        self.initialize_gpio_port(port_num, status)
        
    def initialize_gpio_port(self, port_num, status):
        self.port_num = port_num
        self.status = status
        if not (status == True or status == False):
            raise ValueError('Status needs to be bool')
        GPIO.setup(port_num, GPIO.OUT)
        if self.debug:
            print('GPIO %d initialized for Output' % port_num)
        self.set_status(self.status_to_signal[status])
        
    def toggle(self):
        self.status = not self.status
        self.set_status(self.status)
        
    def set_status(self, status):    
        GPIO.output(self.port_num, self.status_to_signal[status])
        if self.debug:
          print('GPIO %d set to %s' % (self.port_num, 'on' if status else 'off'))

    
