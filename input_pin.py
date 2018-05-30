import RPi.GPIO as GPIO


class InputPin(object):
    """An input pin for GPIO access - keeps track of its status
        
    Attributes:
        port_num: An int for the GPIO port number for this port
        debug: A bool for whether debug messages are output
    """
    
    def __init__(self, port_num, debug = False):
        self.debug = debug
        self.initialize_gpio_port(port_num)
        
    def initialize_gpio_port(self, port_num):
        self.port_num = port_num     
        GPIO.setup(port_num, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        if self.debug:
            print('GPIO %d initialized for Input' % port_num)
        
    def read(self):
        return GPIO.input(self.port_num)
    
    def add_callback(self, edge_type, callback_fn):
        GPIO.add_event_detect(self.port_num, edge_type, callback=callback_fn, bouncetime = 300)

    def wait_for_edge(self, edge_type, bouncetime):
        return GPIO.wait_for_edge(self.port_num, edge_type, bouncetime = bouncetime)
    
    def wait_for_edge_with_timeout(self, edge_type, timeout, bouncetime):
        return GPIO.wait_for_edge(self.port_num, edge_type, timeout = timeout, bouncetime = bouncetime)

    

