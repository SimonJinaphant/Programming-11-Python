'''
	The Sieve of Eratosthenes is an algorithm used to determine
	prime numbers in sequential order
	
	The algorithm starts with creating a collection from the first
	prime number (which is 2) to the highest number you want to test
	
	We start from the first value in the collection, and iterate through the
	collection from the next index, removing any value that is a factor of it
	
	Then increase the factor value by the next number which hasn't been crossed
	out, since we've removed all the numbers that has a factor so far, the next value
	will always be the value in next index
	
'''

maxLimit = int(raw_input("Enter the limit for the prime numbers: "))

primeNumbers = range(2,maxLimit+1)

for index in range(0,int(maxLimit**(0.5))):
	for number in primeNumbers[index+1:]:
		if number % primeNumbers[index] == 0:
			primeNumbers.remove(number)

print "Prime numbers are:"
print primeNumbers