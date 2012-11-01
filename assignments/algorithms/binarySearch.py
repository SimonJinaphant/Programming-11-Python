import random
import time

min = 1
max = 100
count = 1

number = random.randrange(min,max+1)
guess = (max+min)/2

print "\nThe magic number is: ", number
print "let's see how the binary search figures it out"

while True:
	print "\nMininum: ",min,"\tMaximum: ",max
	print "Guess is", guess
	
	time.sleep(1)
	
	if guess == number:
		print "\nBinary Search found it, it's", guess
		print "It only took",count,"attempt(s)"
		break
	elif guess > number:
		print "Too high, reducing search scope"
		max = guess - 1
	elif guess < number:
		print "Too low, increasing search scope"
		min = guess + 1
	
	guess = (max+min)/2
	count+=1