'''
	ASCII House - Even more unnecessarily over complicated version
	Seriously where do I find the time to write these.... >.>
	
	Contains
		- Hex values for characters
		- Unnecessary bit representation for multiplication
		- Unnecessary bit shifting operations like ((0b01<<0b00)+0b00)
		- Super long statement line
	
	September 23 2012
'''
from binascii import unhexlify

x = "\t"		#Only 1 variable needed :)

#--------------------------------------------------------

print x*((0b01 << 0b01)+0b01)+chr(0x2d)*((0b01<<5)-((0b01 << 3)-0b01))

print x*(0b01 << 0b01)+chr(0x20)*((0b01 << 0b10)+0b11)+chr(0x2f)+x*((0b01 << 0b01)+0b01)+chr(0x20)*((0b01 << 0b00)+0b00)+chr(0x5c)  # ((0b01 << 0b00)+0b00) Totally unnecessary right?
print x*(0b01 << 0b01)+chr(0x20)*((0b01 << 0b10)+0b10)+chr(0x2f)+x*((0b01 << 0b10)+0b00)+chr(0x20)*((0b01 << 0b01)+0b00)+chr(0x5c)
print x*(0b01 << 0b01)+chr(0x20)*((0b01 << 0b10)+0b01)+chr(0x2f)+x*((0b01 << 0b10)+0b00)+chr(0x20)*((0b01 << 0b01)+0b01)+chr(0x5c)
print x*(0b01 << 0b01)+chr(0x20)*((0b01 << 0b10)+0b00)+chr(0x2f)+x*((0b01 << 0b10)+0b00)+chr(0x20)*((0b01 << 0b10)+0b00)+chr(0x5c)
print x*(0b01 << 0b01)+chr(0x20)*((0b01 << 0b01)+0b01)+chr(0x2f)+x*((0b01 << 0b10)+0b00)+chr(0x20)*((0b01 << 0b10)+0b01)+chr(0x5c)

print x*(0b01 << 0b01)+chr(0x20)*0b10+chr(0x2d)*((0b01 << 5)+((0b01 << 2)+0b01))

print x*(0b01 << 0b01)+chr(0x20)*(0b01 << 0b01)+chr(0x7c)+x*(0b01 << 0b10)+chr(0x20)*((0b01 << 0b10)+0b10)+chr(0x7c)
print x*(0b01 << 0b01)+chr(0x20)*(0b01 << 0b01)+chr(0x7c)+x*(0b01 << 0b10)+chr(0x20)*((0b01 << 0b10)+0b10)+chr(0x7c)
print x*(0b01 << 0b01)+chr(0x20)*(0b01 << 0b01)+chr(0x7c)+x*(0b01 << 0b10)+chr(0x20)*((0b01 << 0b10)+0b10)+chr(0x7c)

print x*(0b01 << 0b01)+chr(0x20)*(0b01 << 0b01)+chr(0x7c)+x+chr(0x2d)*((0b01 << 0b11)+0b10)+x+chr(0x20)*((0b01 << 0b10)+0b01)+chr(0x2d)*((0b01 << 0b10)+0b11)+chr(0x20)*(0b01 << 0b01)+chr(0x7c)

print x*(0b01 << 0b01)+chr(0x20)*(0b01 << 0b01)+chr(0x7c)+x+chr(0x7c)+chr(0x20)*((0b01 << 0b01)+0b01)+chr(0x7c)+chr(0x20)*(0b01 << 0b10)+chr(0x7c)+x+chr(0x20)*((0b01 << 0b10)+0b01)+chr(0x7c)+chr(0x20)*((0b01 << 0b10)+0b01)+chr(0x7c)+chr(0x20)*(0b01 << 0b01)+chr(0x7c)
print x*(0b01 << 0b01)+chr(0x20)*(0b01 << 0b01)+chr(0x7c)+x+chr(0x7c)+chr(0x2d)*((0b01 << 0b01)+0b01)+chr(0x7c)+chr(0x2d)*(0b01 << 0b10)+chr(0x7c)+x+chr(0x20)*((0b01 << 0b10)+0b01)+chr(0x7c)+chr(0x20)*((0b01 << 0b10)+0b01)+chr(0x7c)+chr(0x20)*(0b01 << 0b01)+chr(0x7c)
print x*(0b01 << 0b01)+chr(0x20)*(0b01 << 0b01)+chr(0x7c)+x+chr(0x7c)+chr(0x20)*((0b01 << 0b01)+0b01)+chr(0x7c)+chr(0x20)*(0b01 << 0b10)+chr(0x7c)+x+chr(0x20)*((0b01 << 0b10)+0b01)+chr(0x7c)+chr(0x20)*((0b01 << 0b10)+0b01)+chr(0x7c)+chr(0x20)*(0b01 << 0b01)+chr(0x7c)

print x*(0b01 << 0b01)+chr(0x20)*(0b01 << 0b01)+chr(0x7c)+x+chr(0x2d)*((0b01 << 0b11)+0b10)+x+chr(0x20)*((0b01 << 0b10)+0b01)+chr(0x7c)+chr(0x20)*((0b01 << 0b10)+0b01)+chr(0x7c)+chr(0x20)*(0b01 << 0b01)+chr(0x7c)

print x*(0b01 << 0b01)+chr(0x20)*(0b01 << 0b01)+chr(0x2d)*((0b01<<5)+((0b01<<2)+0b01))

#----------------------------------------------------------

print "\n"*(0b01 << 0b01)+x*((0b01 << 0b10)+0b10)+chr(0x2d)+chr(0x20)+unhexlify("53696d6f6e204a696e617068616e74")