import random

number = random.randrange(0,101)

while True:
	input = int(raw_input("Enter your guess: "))
	
	if input == number:
		print "Congratz :D"
		break
	elif input < number:
		print "Too low"
	elif input > number:
		print "Too high"