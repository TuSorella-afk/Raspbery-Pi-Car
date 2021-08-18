from flask import Flask
import keyboard

app = Flask(__name__)

@app.route('/')
def start():
    keyPressed = "None"
    while True:  
        try: 
            if keyboard.is_pressed('left arrow'):  
                keyPressed = "Left"
                print("Left")
                break 
            elif keyboard.is_pressed('right arrow'):  
                keyPressed = "Right"
                print("Right")
                break 
            elif keyboard.is_pressed('up arrow'):  
                keyPressed = "Forward"
                print("Forward")
                break 
            elif keyboard.is_pressed('down arrow'):  
                keyPressed = "Backward"
                print("Backward")
                break   
        except:
            return "An error occurred !" 
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
    # </script>"""