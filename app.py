from flask import Flask
import keyboard
import time
import sys

app = Flask(__name__)

# questo blocco evita che flask loggi la gestione delle call al server, 
# quest'ultime sono gestite dalla libreria werkzeug, quindi agiamo su di lei

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# funzione di reload della finestra cosi che rilegga l'input utente continuamente
reloadStatement = "<script>location.reload()</script>" 

@app.route('/')
def start():
    #delay per evitare frame lag
    time.sleep(0.01)  
    try: 
        #visto che sono tutti uguali gli if commento questo
        if keyboard.is_pressed('left arrow'):
            # output in console
            sys.stdout.write("Left\n")
            # forza python a fare output in console dei buffer da scrivere
            sys.stdout.flush() 
            # passa la pagina da renderizzare, semplice html e css nel tag style
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
                                border: 4px solid #008000;
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
                                left: 890px;
                                top: 150px;
                                color: #008000;
                            }
                        </style>
                        <h1 id="pointing">Left</h1>
                        <div id="right"></div>
                        <div id="left"></div>
                        <div id="down"></div>
                        <div id="up"></div>
                        <svg xmlns="http://www.w3.org/2000/svg" id="arrow_downward" viewBox="0 0 16 16">
                            <path fill-rule="evenodd" d="M8 1a.5.5 0 0 1 .5.5v11.793l3.146-3.147a.5.5 0 0 1 .708.708l-4 4a.5.5 0 0 1-.708 0l-4-4a.5.5 0 0 1 .708-.708L7.5 13.293V1.5A.5.5 0 0 1 8 1z"/>
                        </svg>
                        <svg xmlns="http://www.w3.org/2000/svg" id="arrow_back" fill="green" viewBox="0 0 16 16">
                            <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
                        </svg>
                        <svg xmlns="http://www.w3.org/2000/svg" id="arrow_forward" viewBox="0 0 16 16">
                            <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
                        </svg>
                        <svg xmlns="http://www.w3.org/2000/svg" id="arrow_upward" viewBox="0 0 16 16">
                            <path fill-rule="evenodd" d="M8 15a.5.5 0 0 0 .5-.5V2.707l3.146 3.147a.5.5 0 0 0 .708-.708l-4-4a.5.5 0 0 0-.708 0l-4 4a.5.5 0 1 0 .708.708L7.5 2.707V14.5a.5.5 0 0 0 .5.5z"/>
                        </svg>""" + reloadStatement            
                
        elif keyboard.is_pressed('right arrow'):
            sys.stdout.write("Right\n") 
            sys.stdout.flush()  
            return  """<style>
                            #right {
                                position: absolute;
                                width: 150px;
                                height: 150px;
                                left: 992px;
                                top: 453px;
                                background: #FFFFFF;
                                border: 4px solid #0000FF;
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
                                left: 882px;
                                top: 150px;
                                color: #0000FF;
                            }
                        </style>
                        <h1 id="pointing">Right</h1>
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
                        <svg xmlns="http://www.w3.org/2000/svg" id="arrow_forward" fill="blue" viewBox="0 0 16 16">
                            <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
                        </svg>
                        <svg xmlns="http://www.w3.org/2000/svg" id="arrow_upward" viewBox="0 0 16 16">
                            <path fill-rule="evenodd" d="M8 15a.5.5 0 0 0 .5-.5V2.707l3.146 3.147a.5.5 0 0 0 .708-.708l-4-4a.5.5 0 0 0-.708 0l-4 4a.5.5 0 1 0 .708.708L7.5 2.707V14.5a.5.5 0 0 0 .5.5z"/>
                        </svg>""" + reloadStatement
                
        elif keyboard.is_pressed('up arrow'):
            sys.stdout.write("Forward\n")   
            sys.stdout.flush()
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
                                border: 4px solid #800080;
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
                                left: 860px;
                                top: 150px;
                                color: #800080;
                            }
                        </style>
                        <h1 id="pointing">Forward</h1>
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
                        <svg xmlns="http://www.w3.org/2000/svg" id="arrow_upward" fill="purple" viewBox="0 0 16 16">
                            <path fill-rule="evenodd" d="M8 15a.5.5 0 0 0 .5-.5V2.707l3.146 3.147a.5.5 0 0 0 .708-.708l-4-4a.5.5 0 0 0-.708 0l-4 4a.5.5 0 1 0 .708.708L7.5 2.707V14.5a.5.5 0 0 0 .5.5z"/>
                        </svg>""" + reloadStatement
                
        elif keyboard.is_pressed('down arrow'): 
            sys.stdout.write("Backward\n")
            sys.stdout.flush()   
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
                                border: 4px solid #FFA500;
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
                                color: #FFA500;
                            }
                        </style>
                        <h1 id="pointing">Backward</h1>
                        <div id="right"></div>
                        <div id="left"></div>
                        <div id="down"></div>
                        <div id="up"></div>
                        <svg xmlns="http://www.w3.org/2000/svg" id="arrow_downward" fill="orange" viewBox="0 0 16 16">
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
                        </svg>""" + reloadStatement
            
        else:
            sys.stdout.write("None\n")
            sys.stdout.flush()
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
                                left: 883px;
                                top: 150px;
                            }
                        </style>
                        <h1 id="pointing">None</h1>
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
                        </svg>""" + reloadStatement
    except:
        sys.stdout.write("Error\n")
        sys.stdout.flush()
        return "An error occurred !"    
