import RPi.GPIO as GPIO
import time
from CarUtility import *
import subprocess

trigPin = 16
echoPin = 18
ledPin = 11
MAX_DISTANCE = 220

def Destroy():
    Fari.stopFari
    GPIO.cleanup()
    proc.terminate()


def Luce():
    Fari.getFari()


def IoTinputReader(proc):
    # leggi posizione, decodificala da binary ad ASCII, e infine elimina ogni white space
    result = proc.stdout.readline().decode("utf-8").strip()
    if (result == "Left"):
        print("Left")
    elif (result == "Right"):
        print("Right")
    elif (result == "Forward"):
        print("Forward")
    elif (result == "BackWard"):
        print("BackWard")
    elif (result == "None"):
        print("Someone is online")
    elif (result == ""):
        proc.terminate()
    elif (result == "Error"):
        print("\nAn error occured !")
        # termina esecuzione processo
        Destroy()
    return
# chiama il comando 'flask run' da shell/cmd
proc = subprocess.Popen("flask run", stdout=subprocess.PIPE, shell=True)
print("Server running on : http://127.0.0.1:5000/")
if __name__ == '__main__':
    try:
        Fari.setup(ledPin)
        while True:
            IoTinputReader(proc)
            Luce()
    except KeyboardInterrupt:
        Destroy()
