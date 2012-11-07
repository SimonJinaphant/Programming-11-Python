'''
	Finding prime numbers

	- Simon Jinaphant
'''

def isPrimeNumber(number):
	if number < 1:
		print "Invalid number, must be and integer <= 1"
		
	'''
		Test only numbers greater than 5 that isn't even or a factor of 5
			 
		All even numbers are not prime, and numbers < 5 that has a last digit of 5
	    isn't a prime either      
	'''
	if number > 5 and not( number % 2 == 0 or number % 5 == 0):

		if hasNonPrimeFactor(number):
		
			print number, "is a prime number"
			
	elif number in (1,2,3,5):
	
		#Special cases...
		print number, "is a prime number"
	
'''
	Although a linear comparison isn't the fastest way
	it's the most simplest and decent speed way
	
	A faster way would be to mod the number against 
	all prime numbers between 3 and 1/2 of the number
	although that would mean we need to find the prime numbers first >.>
'''
def hasNonPrimeFactor(number):
	'''
		Testing from an increasing low number would be more efficient
		There's a better possibility of a low increasing number being a factor
	'''
	for factor in range(3, number/2):
		
		if factor % 2 == 0 or factor % 5 == 0:
			#All even and factors of five will be ignored
			continue
			
		if number % factor == 0:
			#This number has a factor...so it's not a prime
			return False
	
	'''
		The loop has finished and we are still in the method, therefore
		the number is indeed a prime...unless something went wrong :o
	'''		
	return True
	
for i in range(1,101):
	isPrimeNumber(i)