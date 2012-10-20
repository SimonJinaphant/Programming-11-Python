NO_INPUT = 0b1
KEY_ONLY_INPUT = 0b10
MOUSE_ONLY_INPUT = 0b100
KEY_MOUSE_INPUT = 0b1000


def allowInput(bitValue):
	return bitValue & ~NO_INPUT != 0

def allowMouseInput(bitValue):
	return bitValue & (MOUSE_ONLY_INPUT | KEY_MOUSE_INPUT) != 0

def allowKeyInput(bitValue):
	return bitValue & (KEY_ONLY_INPUT | KEY_MOUSE_INPUT) != 0

print "Input flags:"
print "NO_INPUT = ", NO_INPUT,"\t KEY_ONLY_INPUT = ", KEY_ONLY_INPUT
print "MOUSE_ONLY_INPUT = ", MOUSE_ONLY_INPUT,"\t KEY_MOUSE_INPUT = ", KEY_MOUSE_INPUT

selected = int(raw_input("Enter your input flag: "))

while True:
	if allowInput(selected):
		if allowMouseInput(selected) and allowKeyInput(selected):
			print "You have full input"
			break
		elif allowMouseInput(selected):
			print "You can move your mouse"
		elif allowKeyInput(selected):
			print "You can type"

	else:
		print "You have no input >.>"

	if selected == 0:
		selected = 1
	else:
		selected <<= 1
		
	print "\n---Increasing your input bit---\n"