import subprocess
import keyboard

def IoTinputReader():
    # chiama il comando 'flask run' da shell/cmd
    proc = subprocess.Popen("flask run", stdout=subprocess.PIPE)
    print("Server running on : http://127.0.0.1:5000/")
    while(True):
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
            break
        elif (result == "Error"):
            print("\nAn error occured !")
            proc.terminate()
            break
    return

#IoTinputReader() dovrebbe essere racchiuso secondo questa istruzione :
# import Thread
# t = Thread(target=IoTinputReader) # assegna funzione al thread
# t.start() # fai partire il thread

IoTinputReader()
