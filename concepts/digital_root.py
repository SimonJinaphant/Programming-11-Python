from math import log10, floor

number = int(raw_input("Enter a number: "))

def extract_digits(number): 
	'''
		Mathematically extract digits within a positive integer via logarithm
		
		This is an alternative to converting a number to a string
		and casting it's individual digits back to an integer for
		mathematical operations
	'''

	for i in xrange(int(log10(number)+1), -1, -1):
		'''
			To find the length of a number mathematically, use log10 and add 1
			
			Iterate by counting down, this will get the digits from left to right
			
			To get a digit we use the modulo operation:
				Mod the number by 10^(i+1), where i is the reversed 'index' of the integer
				to get your chosen digit in the lead numerical placement
							
				To get rid of the extra digits we don't need we divide the results above
				by 10^i
				
				This will shift the decimal point to be right after your chosen digit
				Finally floor the result, this will get rid of the remaining digits after
				the decimal point, which will be the extra digits.
		'''
		yield int(floor(number % (10**(i+1))) / (10**(i)))


while number >= 10:
	number = sum(extract_digits(number))
		
print "The digital sum is:", number