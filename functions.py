'''
	Raspberry Pi GPIO Status and Control
'''
import smbus

address1 = 0x20
address2 = 0x21
address3 = 0x22
address4 = 0x23

gleisebyte1 = 0x00
gleisebyte2 = 0x00



bus = smbus.SMBus(1)

def gleis1_hp0():
	global gleisebyte1
	gleisebyte1 = gleisebyte1 | 0b0000000000000001
	print(gleisebyte1)
	bus.write_byte(address1,gleisebyte1)
	
def gleis1_hp1():
	global gleisebyte1
	gleisebyte1 = gleisebyte1 & 0b0000000011111110
	print(gleisebyte1)
	bus.write_byte(address1,gleisebyte1)
	
def gleis2_hp0():
	global gleisebyte1
	gleisebyte1 = gleisebyte1 | 0b0000000000000010
	print(gleisebyte1)
	bus.write_byte(address1,gleisebyte1)
	
def gleis2_hp1():
	global gleisebyte1
	gleisebyte1 = gleisebyte1 & 0b0000000011111101
	print(gleisebyte1)
	bus.write_byte(address1,gleisebyte1)

def gleis3_hp0():
	global gleisebyte1
	gleisebyte1 = gleisebyte1 | 0b0000000000000100
	print(gleisebyte1)
	bus.write_byte(address1,gleisebyte1)
	
def gleis3_hp1():
	global gleisebyte1
	gleisebyte1 = gleisebyte1 & 0b0000000011111011
	print(gleisebyte1)
	bus.write_byte(address1,gleisebyte1)

def gleis4_hp0():
	global gleisebyte1
	gleisebyte1 = gleisebyte1 | 0b0000000000001000
	print(gleisebyte1)
	bus.write_byte(address1,gleisebyte1)

def gleis4_hp1():
	global gleisebyte1
	gleisebyte1 = gleisebyte1 & 0b0000000011110111
	print(gleisebyte1)
	bus.write_byte(address1,gleisebyte1)
	
def gleis5_hp0():
	global gleisebyte1
	gleisebyte1 = gleisebyte1 | 0b0000000000010000
	print(gleisebyte1)
	bus.write_byte(address1,gleisebyte1)	
	
def gleis5_hp1():
	global gleisebyte1
	gleisebyte1 = gleisebyte1 & 0b0000000011101111
	print(gleisebyte1)
	bus.write_byte(address1,gleisebyte1)

def gleis6_hp0():
	global gleisebyte1
	gleisebyte1 = gleisebyte1 | 0b0000000000100000
	print(gleisebyte1)
	bus.write_byte(address1,gleisebyte1)

def gleis6_hp1():
	global gleisebyte1
	gleisebyte1 = gleisebyte1 & 0b0000000011011111
	print(gleisebyte1)
	bus.write_byte(address1,gleisebyte1)

def gleis7_hp0():
	global gleisebyte1
	gleisebyte1 = gleisebyte1 | 0b0000000001000000
	print(gleisebyte1)
	bus.write_byte(address1,gleisebyte1)

def gleis7_hp1():
	global gleisebyte1
	gleisebyte1 = gleisebyte1 & 0b0000000010111111
	print(gleisebyte1)
	bus.write_byte(address1,gleisebyte1)

def gleis8_hp0():
	global gleisebyte1
	gleisebyte1 = gleisebyte1 | 0b0000000010000000
	print(gleisebyte1)
	bus.write_byte(address1,gleisebyte1)

def gleis8_hp1():
	global gleisebyte1
	gleisebyte1 = gleisebyte1 & 0b0000000001111111
	print(gleisebyte1)
	bus.write_byte(address1,gleisebyte1)




