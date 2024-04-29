import RPi.GPIO as GPIO
import subprocess
from time import sleep , time

# Motor controller pin
# Motor situation
FORWARD  = 1
BACKWORD = 2
RIGHT = 3
LEFT = 4
STOP = 5
# Motor channel
CH1 = 0
CH2 = 1

# PIN set
# PWM PIN
ENA = 26  #37 pin
ENB = 20   #38 pin
# MOTOR GPIO PIN
IN1 = 19  #35 pin
IN2 = 13  #33 pin
IN3 = 6   #31 pin
IN4 = 5   #29 pin
# BUTTON GPIO PIN
BUTTON_ON_PIN = 21
BUTTON_OFF_PIN = 17
# ECHO SENSOR GPIO PIN
TRIGGER = 23
ECHO = 24

# Set Pin(Motor)
def setPinConfig(EN, INA, INB):        
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)
    GPIO.setup(INB, GPIO.OUT)
    # Work PWM 100khz
    pwm = GPIO.PWM(EN, 100) 
    # Stop PWM   
    pwm.start(0) 
    return pwm
# Motor control function
def setMotorControl(pwm, INA, INB, speed, stat):
    # Motor speed control PWM
    pwm.ChangeDutyCycle(speed)  
    if stat == FORWARD:
        GPIO.output(INA, GPIO.HIGH)
        GPIO.output(INB, GPIO.LOW)
    elif stat == BACKWORD:
        GPIO.output(INA, GPIO.LOW)
        GPIO.output(INB, GPIO.HIGH)
    elif stat == STOP:
        GPIO.output(INA, GPIO.LOW)
        GPIO.output(INB, GPIO.LOW)
# Motor control function rapping
def setMotor(ch, speed, stat):
    if ch == CH1:
        setMotorControl(pwmA, IN1, IN2, speed, stat)
    else:
        setMotorControl(pwmB, IN3, IN4, speed, stat)
# double Motor control function
def setIntegratedControl(stat):
    if stat == STOP:
            setMotor(CH1,20,STOP)
            setMotor(CH2,20,STOP)
            sleep(3)
            setMotor(CH1,20,BACKWORD)
            setMotor(CH2,20,FORWARD)
            sleep(6)

    if stat == RIGHT:
        setMotor(CH1,50,BACKWORD)
        setMotor(CH2,50,STOP)
        
    if stat == LEFT:
        setMotor(CH1,50,STOP)
        setMotor(CH2,50,FORWARD)
        sleep(5)

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

def start_process(channel):
    global process
    if process is None: 
        print("Process starting...")
        process = subprocess.Popen(['python3', '/home/eee/yolov5/111.py'])
    else:
        print("Process is already running.")

def stop_process(channel):
    global process
    if process is not None: 
        print("Terminating process...")
        process.terminate() 
    else:
        print("No process is running.")

if __name__ == "__main__":      
    # Set Control
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIGGER,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    # Motor PWM set
    pwmA = setPinConfig(ENA, IN1, IN2)
    pwmB = setPinConfig(ENB, IN3, IN4)

    # Button Start set
    GPIO.setup(BUTTON_ON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BUTTON_OFF_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    process = None
    GPIO.add_event_detect(BUTTON_ON_PIN, GPIO.RISING, callback=start_process, bouncetime=300)
    GPIO.add_event_detect(BUTTON_OFF_PIN, GPIO.RISING, callback=stop_process, bouncetime=300)

    try:
        while True:
            sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()