import subprocess

def IoTinputReader():
    proc = subprocess.Popen("flask run", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print("Server running on : http://127.0.0.1:5000/")
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
        print(result.decode("utf-8"))

IoTinputReader()