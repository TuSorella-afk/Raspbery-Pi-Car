from flask import Flask
from flask import request
import keyboard

app = Flask(__name__)

@app.route('/')
def start():
    keyPressed = "None"
    while True:  
        try: 
            if keyboard.is_pressed('left arrow'):  
                keyPressed = "Left"
                break 
            elif keyboard.is_pressed('right arrow'):  
                keyPressed = "Right"
                break 
            elif keyboard.is_pressed('up arrow'):  
                keyPressed = "forward"
                break 
            elif keyboard.is_pressed('down arrow'):  
                keyPressed = "backward"
                break   
        except:
            keyPressed = "None"
            break
    return f"<h1 style = 'text-align:center; margin-top:250px;'>Actual pointing : {keyPressed}</h1><script>location.reload()</script>"
    # return """
    # <h1 id = 'pointing' style = 'text-align:center; margin-top:250px;'>Actual pointing : Null</h1>
    # <script>document.addEventListener('keydown', function(e) {
    # switch (e.keyCode) {
    #     case 37:
    #         document.getElementById("pointing").innerHTML = "Actual pointing : left";
    #         break;
    #     case 38:
    #         document.getElementById('pointing').innerHTML = 'Actual pointing : forward';
    #         break;
    #     case 39:
    #         document.getElementById('pointing').innerHTML = 'Actual pointing : right';
    #         break;
    #     case 40:
    #         document.getElementById('pointing').innerHTML = 'Actual pointing : backward';
    #         break;
    #     }
    # });
    # </scrip>"""

@app.route('/forward', methods=['POST'])
def front():
    if request.method == 'POST':
        return "avanti"
    else:
        return "error"

@app.route('/backward', methods=['POST'])
def back():
    if request.method == 'POST':
        return "indietro"
    else:
        return "error"

@app.route('/left', methods=['POST'])
def left():
    if request.method == 'POST':
        return "sinistra"
    else:
        return "error"

@app.route('/right', methods=['POST'])
def right():
    if request.method == 'POST':
        return "destra"
    else:
        return "error"