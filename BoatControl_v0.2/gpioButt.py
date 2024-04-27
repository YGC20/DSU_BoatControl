import RPi.GPIO as GPIO
import subprocess
from time import sleep

# BUTTON GPIO PIN
BUTTON_ON_PIN = 21
BUTTON_OFF_PIN = 17

process = None

def start_process(channel):
    global process
    if process is None: 
        print("Process starting...")
        process = subprocess.Popen(['python3', '/home/eee/yolov5/yoloRun.py'])
    else:
        print("Process is already running.")

def stop_process(channel):
    global process
    if process is not None: 
        print("Terminating process...")
        process.terminate() 
    else:
        print("No process is running.")

# Set Control
GPIO.setmode(GPIO.BCM)
# Button Start set
GPIO.setup(BUTTON_ON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_OFF_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(BUTTON_ON_PIN, GPIO.RISING, callback=start_process, bouncetime=300)
GPIO.add_event_detect(BUTTON_OFF_PIN, GPIO.RISING, callback=stop_process, bouncetime=300)

try:
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()