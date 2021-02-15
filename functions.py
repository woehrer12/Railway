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
