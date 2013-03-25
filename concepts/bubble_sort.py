def bubble_sort(unsorted):
	changed = True
	
	while changed:
	
		changed = False
		
		for i in xrange(1, len(unsorted)):
			print unsorted[i]
			print unsorted[i-1]
			print
			if unsorted[i-1] > unsorted[i]:
				unsorted[i], unsorted[i-1] = unsorted[i-1], unsorted[i]
				changed = True
				
	return unsorted
			
			
def bubble_sort2(unsorted):
	for k in xrange(1, len(unsorted)):
		for i in xrange(len(unsorted) - k):
			print "Current list: {0}\n\tComparing {1} and {2}".format(unsorted, unsorted[i], unsorted[i+1])

			if unsorted[i+1] < unsorted[i]:
				print "\t{0} is greater than {1}: swaping places\n".format(unsorted[i], unsorted[i+1])
				unsorted[i], unsorted[i+1] = unsorted[i+1], unsorted[i]
			else:
				print "\t{0} is less than or equal to {1}: moving on...\n".format(unsorted[i], unsorted[i+1])
				
	return unsorted
	

print bubble_sort2([607,6,80,23,56,201])