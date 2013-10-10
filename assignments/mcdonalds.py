'''
	McDonalds Solution

	We can define two varaiable to start off:
	one to hold the total amount of money we have overall
	another one to hold the payment we get by the end of the day

	We would need these variables because their values will change
	and we need to know what it holds over time
'''
total_earned = 0
payment = 0.01


'''
	Next we go into a loop that will cycle 30 times (Which represents 30 days of working)
	In each each cycle (or in each work day) we do the following:
		1) add what we earn to the total sum
		2) double our payment for next day
	Note: If you double your payment BEFORE adding, your total will end up be double of what you should get
'''
for _day in range(30):
	total_earned += payment
	payment *= 2

'''
	And finally we print out the amount of money the gullible manager owes us :)
'''
print total_earned





'''
	Another note: Notice that in this version of the solution, the for loop varaiable _day 
	wasn't used in the loop, this is because everytime you create a for loop you
	DON'T ALWAYS HAVE TO USE the variable. The variable is there only to satisfy Python's syntax rules.

	In Python if you see a variable name begining with an underscore _ :
	know that it is a language CONVENTION used to tell other programmers who read the code that:
	"this variable isn't intented to be used (it's a throwaway) but needs to exist to make the syntax valid"

	If, for some reason, you wanted to use the day variable in your calculation you could also do:
	total = 0

	for day in range(30):
		total += (0.01 * 2**day)

	print total

	There's many ways you can do this assignment, it all depends of which way you feel comfortable with.

----------------------------------------------------------------------------------------

	OPTIONAL CHALLENGE
	For anyone who found this assignment way too easy and wants to GO BEYOND THE COURSE expectations,
	Try to figure out how this one line code gives the same output:
	
	print ((1 << 30)-1)/100.0

	Where 30 is the day we need to work and 1 is the payment amount we start with, in cents

	Hint: Google is a great friend when you're learning on your own :)
'''