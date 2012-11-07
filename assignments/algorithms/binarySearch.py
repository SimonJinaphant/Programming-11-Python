import random
import time

min = 1
max = 100
count = 1

number = random.randrange(min,max+1)
guess = (max+min)/2

print "\nThe magic number is: ", number
print "let's see how the binary search figures it out"

'''
	A binary search isn't truly infinite 
	(so using "while true" may not be the best idea...)
	
	From my analysis it seems to correspond to the most significant 
	bit of the number being the maximum number of times we have to check for it
'''
while True:
	print "\nMininum: ", min, "\tMaximum: ", max
	print "Guess is", guess
	
	#Sleeping to show the process in a dramatic way :D
	time.sleep(1)
	
	if guess == number:
		print "\nBinary Search found it, it's", guess
		print "It only took", count, "attempt(s)"
		break
	elif guess > number:
		print "Too high, reducing search scope"
		max = guess - 1
	else:
		print "Too low, increasing search scope"
		min = guess + 1

	guess = (max+min)/2
	count+=1