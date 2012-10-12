sum = 0
while True:
	input = int(raw_input("Enter: "))
	if input == 0:
		break
	else:
		sum += input
		print "Total", sum

print "Program exited with total of", sum
