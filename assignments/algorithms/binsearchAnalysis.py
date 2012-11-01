import random
import time


for i in range(1,101):
	
	min = 1
	max = 100
	count = 1
	number = i
	#number = random.randrange(min,max+1)
	guess = (max+min)/2
	
	
	while True:
		'''print "\nMininum: ",min,"\tMaximum: ",max
		print "Guess is", guess
	
		time.sleep(1)
		'''
		if guess == number:
			print "\nBinary Search found it, it's", guess
			print "It only took",count,"attempt(s)"
			break
		elif guess > number:
			#print "Too high, reducing search scope"
			max = guess - 1
		elif guess < number:
			#print "Too low, increasing search scope"
			min = guess + 1
	
		guess = (max+min)/2
		count+=1
		
	