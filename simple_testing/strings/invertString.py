inputString = raw_input("Enter a string: ")
outputString = ""

for letter in inputString:

	if letter >= chr(0x41) and letter <= chr(0x5a):
		outputString += chr(ord(letter)+0x20)
		
	elif letter >= chr(0x61) and letter <= chr(0x7a):
		outputString += chr(ord(letter)-0x20)
		
	else:
		outputString += letter
		
print outputString