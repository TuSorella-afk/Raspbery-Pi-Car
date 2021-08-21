from flask import Flask, request
import keyboard
import time
import sys

app = Flask(__name__)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

print("Server running on : http://127.0.0.1:5000/")

@app.route('/')
def start():
    return  """<style>
                    #right {
                        position: absolute;
                        width: 150px;
                        height: 150px;
                        left: 992px;
                        top: 453px;
                        background: #FFFFFF;
                        border: 4px solid #000000;
                        box-sizing: border-box;
                        border-radius: 20px;
                    }
                    #up {
                        position: absolute;
                        width: 150px;
                        height: 150px;
                        left: 842px;
                        top: 303px;
                        background: #FFFFFF;
                        border: 4px solid #000000;
                        box-sizing: border-box;
                        border-radius: 20px;
                    }
                    #down {
                        position: absolute;
                        width: 150px;
                        height: 150px;
                        left: 842px;
                        top: 453px;
                        background: #FFFFFF;
                        border: 4px solid #000000;
                        box-sizing: border-box;
                        border-radius: 20px;
                    }
                    #left {
                        position: absolute;
                        width: 150px;
                        height: 150px;
                        left: 692px;
                        top: 453px;
                        background: #FFFFFF;
                        border: 4px solid #000000;
                        box-sizing: border-box;
                        border-radius: 20px;
                    }
                    #arrow_downward {
                        position: absolute;
                        width: 100px;
                        height: 100px;
                        left: 867px;
                        top: 478px;
                    }
                    #arrow_forward {
                        position: absolute;
                        width: 100px;
                        height: 100px;
                        left: 1017px;
                        top: 478px;
                    }
                    #arrow_upward {
                        position: absolute;
                        width: 100px;
                        height: 100px;
                        left: 867px;
                        top: 328px;
                    }
                    #arrow_back {
                        position: absolute;
                        width: 100px;
                        height: 100px;
                        left: 717px;
                        top: 478px;
                    }
                    #pointing{
                        position: absolute;   
                        left: 850px;
                        top: 150px;
                    }
                </style>
                <h1 id="pointing">Backward</h1>
                <div id="right"></div>
                <div id="left"></div>
                <div id="down"></div>
                <div id="up"></div>
                <svg xmlns="http://www.w3.org/2000/svg" id="arrow_downward" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 1a.5.5 0 0 1 .5.5v11.793l3.146-3.147a.5.5 0 0 1 .708.708l-4 4a.5.5 0 0 1-.708 0l-4-4a.5.5 0 0 1 .708-.708L7.5 13.293V1.5A.5.5 0 0 1 8 1z"/>
                </svg>
                <svg xmlns="http://www.w3.org/2000/svg" id="arrow_back" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
                </svg>
                <svg xmlns="http://www.w3.org/2000/svg" id="arrow_forward" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
                </svg>
                <svg xmlns="http://www.w3.org/2000/svg" id="arrow_upward" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 15a.5.5 0 0 0 .5-.5V2.707l3.146 3.147a.5.5 0 0 0 .708-.708l-4-4a.5.5 0 0 0-.708 0l-4 4a.5.5 0 1 0 .708.708L7.5 2.707V14.5a.5.5 0 0 0 .5.5z"/>
                </svg>
                <script>
                    function reset(arrow, direction){
                        document.getElementById(arrow).style.fill = "black";
                        document.getElementById("pointing").style.color = "#000000";
                        document.getElementById(direction).style.borderColor = "#000000";
                    }

                    function post(data, key){
                        let url = "http://127.0.0.1:5000/keyCode";
                        let xhr = new XMLHttpRequest();
                        xhr.open("POST", url);
                        xhr.setRequestHeader("Accept", "application/json");
                        xhr.setRequestHeader("Content-Type", "application/json");
                        var timerStart = Date.now();
                        xhr.onreadystatechange = function () {
                            if (xhr.readyState === 4) {
                                console.log(xhr.status);
                                console.log(xhr.responseText);
                                console.log("Load time : " + Date.now()-timerStart.toString());
                                if (key == "left") {
                                    document.getElementById("arrow_back").style.fill = "green";
                                    document.getElementById("pointing").innerHTML = "Left";
                                    document.getElementById("pointing").style.color = "#008000";
                                    document.getElementById("pointing").style.left = "890px";
                                    document.getElementById("left").style.borderColor = "#008000";
                                    setTimeout(reset("arrow_back", "left"), 100);
                                } else if (key == "right") {
                                    document.getElementById("arrow_forward").style.fill = "blue";
                                    document.getElementById("pointing").innerHTML = "Right";
                                    document.getElementById("pointing").style.color = "#0000FF";
                                    document.getElementById("pointing").style.left = "882px";
                                    document.getElementById("right").style.borderColor = "#0000FF";
                                    setTimeout(reset("arrow_forward", "right"), 100);
                                } else if (key == "forward") {
                                    document.getElementById("arrow_upward").style.fill = "purple";
                                    document.getElementById("pointing").innerHTML = "Forward";
                                    document.getElementById("pointing").style.color = "#800080";
                                    document.getElementById("pointing").style.left = "860px";
                                    document.getElementById("up").style.borderColor = "#800080";
                                    setTimeout(reset("arrow_upward", "up"), 100);
                                } else if (key == "backward") {
                                    document.getElementById("arrow_downward").style.fill = "orange";
                                    document.getElementById("pointing").innerHTML = "Backward";
                                    document.getElementById("pointing").style.color = "#FFA500";
                                    document.getElementById("pointing").style.left = "850px";
                                    document.getElementById("down").style.borderColor = "#FFA500";
                                    setTimeout(reset("arrow_downward", "down"), 100);
                                } else if (key == "none") {
                                    document.getElementById("pointing").innerHTML = "None";
                                    document.getElementById("pointing").style.left = "883px";
                                }
                            }};
                        xhr.send(data);
                    }

                    document.addEventListener('keydown', function(event) {
                        if (event.keyCode == 37) {
                            post({'Key' : "left",}, "left");
                        } else if (event.keyCode == 39) {
                            post({'Key' : "right",}, "right");
                        } else if (event.keyCode == 38) {
                            post({'Key' : "forward",}, "forward");
                        } else if (event.keyCode == 40) {
                            post({'Key' : "down",}, "down");
                        } else {
                            post({'Key' : "none",}, "none");
                        }
                    });
                </script>"""

@app.route('/keyCode', methods=["POST"])
def post():
    key = request.form.get("Key")
    print("key : ", end = "")
    print(key)
    if (key == "left"):
        sys.stdout.write("Left\n")
        sys.stdout.flush()
        return "Key found", 200
    elif (key == "right"):
        sys.stdout.write("Right\n") 
        sys.stdout.flush()
        return "Key found", 200    
    elif (key == "forward"):
        sys.stdout.write("Forward\n")   
        sys.stdout.flush()
        return "Key found", 200  
    elif (key == "backward"):
        sys.stdout.write("Backward\n")
        sys.stdout.flush()
        return "Key found", 200  
    elif (key == "none"):
        sys.stdout.write("None\n")
        sys.stdout.flush()
        return "Key found", 200
    else:
        sys.stdout.write("Error\n")
        sys.stdout.flush()
        return "Error 404 : Key invalid", 404