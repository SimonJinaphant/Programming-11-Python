factorialIndex = int(raw_input("Enter the term number: "))

def factorialByRecursion(index):
	if index <= 1:
		return 1;
	
	return factorialByRecursion(index-1)*index
	
def factorialByLoop(index):
	total = 1
	
	for i in range(2,factorialIndex+1):
		total *= i
	
	return total
	
print "From recursion:", factorialByRecursion(factorialIndex)
print "From normal looping:", factorialByLoop(factorialIndex)