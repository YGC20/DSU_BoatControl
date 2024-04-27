import RPi.GPIO as GPIO
from time import sleep , time

# ECHO SENSOR GPIO PIN
TRIGGER = 23
ECHO = 24
# GPIO Set
GPIO.setup(TRIGGER,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def get_distance():
    GPIO.output(TRIGGER,False)
    sleep(0.5)
        
    GPIO.output(TRIGGER,True)
    sleep(0.00001)
    GPIO.output(TRIGGER,False)
        
    while GPIO.input(ECHO) == 0:
        start = time()
            
    while GPIO.input(ECHO) == 1:
        stop = time()
            
    time_interval = stop - start
    distance = time_interval * 17000
    distance = round(distance, 2)
    return distance


