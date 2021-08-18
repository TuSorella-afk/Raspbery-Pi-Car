import RPi.GPIO as GPIO
import time
from CarUtility import *
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


if __name__ == '__main__':
    try:
        Fari.setup(ledPin)
        while True:
            SonarPosition(trigPin, echoPin, MAX_DISTANCE)
            Luce()
    except KeyboardInterrupt:
        Fari.stopFari
        GPIO.cleanup()
