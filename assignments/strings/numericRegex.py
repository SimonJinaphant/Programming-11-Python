import re

def getCollection():
	input = raw_input("Enter a series of numbers separated by a comma: ").strip()
	input = re.sub("[A-Za-z]","",input)
	return eval(input)
		

output = getCollection()
print type(output), output
