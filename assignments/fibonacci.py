from math import sqrt

'''
	Method 1 - Recursion
	Recursion is not the best way to solve this if the index number is very high...
	However it's the most simplest way to explain the solution
'''

def fibonacciByRecursion(index):
	if index <= 2:
		if index <= 0:
			return 0
		return 1
	
	return fibonacciByRecursion(index-1) + fibonacciByRecursion(index-2)
	
'''
	Method 2 - Math
	This method is the preferred way of calculating fibonacci numbers since 
	we won't be creating a large stacking method call every time the index is large
'''

def fibonacciByMath(index):
	squareFive = sqrt(5)
	goldenRatio = (1 + squareFive)/2.0
	otherRatio = -(goldenRatio-1)
	
	return int(((goldenRatio**index)-(otherRatio**index))/squareFive)

'''-----------The real program starts here----------'''

maxIndex = int(raw_input("Enter the maximum index: "))

print '''-----Calculating by math-----
This should be fast even if you've entered a high number :D\n\n'''

for count in range(0,maxIndex):
	print fibonacciByMath(count),

print '''\n\n
-----Calculating by recursion-----
This can be very slow if you have entered a high number...\n\n'''

for count2 in range(0,maxIndex):
	print fibonacciByRecursion(count2),
	
print "\n\n\nWe are Done"