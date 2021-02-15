'''
	Raspberry Pi GPIO Status and Control
'''
import RPi.GPIO as GPIO
from flask import Flask, render_template, request
import smbus
import functions

address1 = 0x20
address2 = 0x21
address3 = 0x22
address4 = 0x23

gleisebyte1 = 0x00
gleisebyte2 = 0x00

bus = smbus.SMBus(1)

Gleis1Signal = "unbekannt"
Gleis2Signal = "unbekannt"
Gleis3Signal = "unbekannt"
Gleis4Signal = "unbekannt"
Gleis5Signal = "unbekannt"
Gleis6Signal = "unbekannt"
Gleis7Signal = "unbekannt"
Gleis8Signal = "unbekannt"


app = Flask(__name__)

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
			gleisebyte1 = gleisebyte1 | 0b0000000000000010
			print(gleisebyte1)
			bus.write_byte(address1,gleisebyte1)
		
		if action == "HP1":
			gleisebyte1 = gleisebyte1 & 0b0000000011111101
			print(gleisebyte1)
			bus.write_byte(address1,gleisebyte1)


	if deviceName == 'Gleis3':
		print("Gleis3")
		if action == "HP0":
			gleisebyte1 = gleisebyte1 | 0b0000000000000100
			print(gleisebyte1)
			bus.write_byte(address1,gleisebyte1)
		
		if action == "HP1":
			gleisebyte1 = gleisebyte1 & 0b0000000011111011
			print(gleisebyte1)
			bus.write_byte(address1,gleisebyte1)
			

	if deviceName == 'Gleis4':
		print("Gleis4")
		if action == "HP0":
			gleisebyte1 = gleisebyte1 | 0b0000000000001000
			print(gleisebyte1)
			bus.write_byte(address1,gleisebyte1)
		
		if action == "HP1":
			gleisebyte1 = gleisebyte1 & 0b0000000011110111
			print(gleisebyte1)
			bus.write_byte(address1,gleisebyte1)
			

	if deviceName == 'Gleis5':
		print("Gleis5")
		if action == "HP0":
			gleisebyte1 = gleisebyte1 | 0b0000000000010000
			print(gleisebyte1)
			bus.write_byte(address1,gleisebyte1)
		
		if action == "HP1":
			gleisebyte1 = gleisebyte1 & 0b0000000011101111
			print(gleisebyte1)
			bus.write_byte(address1,gleisebyte1)


	if deviceName == 'Gleis6':
		print("Gleis6")
		if action == "HP0":
			gleisebyte1 = gleisebyte1 | 0b0000000000100000
			print(gleisebyte1)
			bus.write_byte(address1,gleisebyte1)
		
		if action == "HP1":
			gleisebyte1 = gleisebyte1 & 0b0000000011011111
			print(gleisebyte1)
			bus.write_byte(address1,gleisebyte1)


	if deviceName == 'Gleis7':
		print("Gleis7")
		if action == "HP0":
			gleisebyte1 = gleisebyte1 | 0b0000000001000000
			print(gleisebyte1)
			bus.write_byte(address1,gleisebyte1)
		
		if action == "HP1":
			gleisebyte1 = gleisebyte1 & 0b0000000010111111
			print(gleisebyte1)
			bus.write_byte(address1,gleisebyte1)


	if deviceName == 'Gleis8':
		print("Gleis8")
		if action == "HP0":
			gleisebyte1 = gleisebyte1 | 0b0000000010000000
			print(gleisebyte1)
			bus.write_byte(address1,gleisebyte1)
		
		if action == "HP1":
			gleisebyte1 = gleisebyte1 & 0b0000000001111111
			print(gleisebyte1)
			bus.write_byte(address1,gleisebyte1)



   

   
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
