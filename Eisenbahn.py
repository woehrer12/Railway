'''
	Raspberry Pi GPIO Status and Control
'''
# import RPi.GPIO as GPIO
from flask import Flask, render_template, request

import functions
import threading
import time

from Gleis_Class import Gleis
Gleis1 = Gleis()
Gleis2 = Gleis()
Gleis3 = Gleis()
Gleis4 = Gleis()
Gleis5 = Gleis()
Gleis6 = Gleis()
Gleis7 = Gleis()
Gleis8 = Gleis()

Gleis1Signal = "unbekannt"
Gleis2Signal = "unbekannt"
Gleis3Signal = "unbekannt"
Gleis4Signal = "unbekannt"
Gleis5Signal = "unbekannt"
Gleis6Signal = "unbekannt"
Gleis7Signal = "unbekannt"
Gleis8Signal = "unbekannt"


app = Flask(__name__)

def loop():
	while True:
		print("Looping")
		time.sleep(1)

@app.route("/")
def index():
	# Read Sensors Status
	templateData = {
              'title' : 'Eisenbahn 1!',
              'Gleis1'  : Gleis1Signal,
              'Gleis2'  : Gleis2Signal,
              'Gleis3'  : Gleis3Signal,
              'Gleis4'  : Gleis4Signal,
              'Gleis5'  : Gleis5Signal,
              'Gleis6'  : Gleis6Signal,
              'Gleis7'  : Gleis7Signal,
              'Gleis8'  : Gleis8Signal
        }
	return render_template('index.html', **templateData)
	
@app.route("/<deviceName>/<action>")
def action(deviceName, action):

	if deviceName == 'Gleis1':
		global gleisebyte1
		print("Gleis1")
		if action == "HP0":
			functions.gleis1_hp0()
		if action == "HP1":
			functions.gleis1_hp1()

	if deviceName == 'Gleis2':
		print("Gleis2")
		if action == "HP0":
			functions.gleis2_hp0()
		if action == "HP1":
			functions.gleis2_hp1()

	if deviceName == 'Gleis3':
		print("Gleis3")
		if action == "HP0":
			functions.gleis3_hp0()
		if action == "HP1":
			functions.gleis3_hp1()
			
	if deviceName == 'Gleis4':
		print("Gleis4")
		if action == "HP0":
			functions.gleis4_hp0()
		if action == "HP1":
			functions.gleis4_hp1()
			
	if deviceName == 'Gleis5':
		print("Gleis5")
		if action == "HP0":
			functions.gleis5_hp0()
		if action == "HP1":
			functions.gleis5_hp1()

	if deviceName == 'Gleis6':
		print("Gleis6")
		if action == "HP0":
			functions.gleis6_hp0()
		if action == "HP1":
			functions.gleis6_hp1()

	if deviceName == 'Gleis7':
		print("Gleis7")
		if action == "HP0":
			functions.gleis7_hp0()
		if action == "HP1":
			functions.gleis7_hp1()

	if deviceName == 'Gleis8':
		print("Gleis8")
		if action == "HP0":
			functions.gleis8_hp0()
		if action == "HP1":
			functions.gleis8_hp1()

	if deviceName == 'Start':
		t1 = threading.Thread(target=loop())
		t1.start()



   
	templateData = {
              'title' : 'Eisenbahn 1!',
              'Gleis1'  : Gleis1Signal,
              'Gleis2'  : Gleis2Signal,
              'Gleis3'  : Gleis3Signal,
              'Gleis4'  : Gleis4Signal,
              'Gleis5'  : Gleis5Signal,
              'Gleis6'  : Gleis6Signal,
              'Gleis7'  : Gleis7Signal,
              'Gleis8'  : Gleis8Signal
	}
	return render_template('index.html', **templateData)
	
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=3000, debug=True)

#Bitoperationen
#https://www.webmasterpro.de/coding/article/bit-operationen-in-python.html
