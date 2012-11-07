'''
	All numbers > 10 has a possibility of being a prime when the last digit is 1,3,7,9
	
'''

for number in range(1,101):
	if number > 10:
		if number % 2 == 0 or number % 5 == 0:
			continue
		else:
			
			prime = None
			factor = number/2
			
			while True:
				if factor < 2:
					break
					
				elif number % factor == 0:
					prime = None
					break
					
				else:
					prime = number
					
				factor -= 1

				
			if prime != None:
				print prime

	else:
		if number in (1,2,3,5,7):
			print number