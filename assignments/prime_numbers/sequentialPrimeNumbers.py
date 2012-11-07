'''
	Maximum efficiency (that I can think of) in printing 
	prime numbers IN SEQUENTIAL ORDER
	
	- Simon Jinaphant
'''

primeFactors = [1,2,3,5]
'''
	Unfortunately to maximize efficiency I need to place in the starting 4 values
	since they are exception my algorithm's rules
'''

def printPrimeNumbers():
	for number in range(7,101):
		
		'''
			Test numbers starting from 7 that isn't even or a factor of 5
			 
			All even numbers are not prime, and numbers < 5 that has a last digit of 5
	    	isn't a prime either      
		'''
		if not(number % 2 == 0 or number % 5 == 0):
			hasNonPrimeFactor(number)
				
def hasNonPrimeFactor(number):
	'''
		Only works if the prime factor has already been recorded
		Hence determining a large number itself without any previous
		invoke of this method will result in an error.
	'''
	
	for primeFactor in primeFactors[2:]:
		if number % primeFactor == 0:
			#This number has a prime factor...so it's not a prime
			return False
	
	primeFactors.append(number)

	'''
		The loop has finished and we are still in the method, therefore
		the number is indeed a prime...unless something went wrong :o
		like someone using this method without invoking it on previous numbers
	'''		

printPrimeNumbers()
print "Prime numbers from 1 to 100 are \n", primeFactors