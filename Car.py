import RPi.GPIO as GPIO
import time
from CarUtility import *
import subprocess

trigPin = 16
echoPin = 18
ledPin = 11
MAX_DISTANCE = 220
def Luce():
    Fari.getFari()

def SonarPosition(trigPin, echoPin, MAX_DISTANCE):
    distance = Sonar.getDistance(trigPin, echoPin, MAX_DISTANCE)
    if distance > 5:
        print('Motore avanti')
    else:
        print('motore indietro')

def IoTinputReader():
    proc = subprocess.Popen("flask run", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while(True):
        retcode = proc.poll() 
        result = proc.stdout.readline()
        if (result.decode("utf-8") == "Left"):
            print("Left")
        elif (result.decode("utf-8") == "Right"):
            print("Right")
        elif (result.decode("utf-8") == "Forward"):
            print("Forward")
        elif (result.decode("utf-8") == "BackWard"):
            print("BackWard")

if __name__ == '__main__':
    try:
        Fari.setup(ledPin)
        while True:
            SonarPosition(trigPin, echoPin, MAX_DISTANCE)
            Luce()
    except KeyboardInterrupt:
        Fari.stopFari
        GPIO.cleanup()
