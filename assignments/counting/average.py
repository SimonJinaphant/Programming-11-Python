i = 0
total = 0
while True:
	input = int(raw_input("Enter: "))
	if (input == 0):
		break
	else:
		i+=1
		total += input

print "Average is", total/i
