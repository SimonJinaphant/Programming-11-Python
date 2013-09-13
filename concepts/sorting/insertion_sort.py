def insertion_sort(unsorted):
	for i in xrange(1, len(unsorted)):
		for j in xrange(i, 0, -1):
			if unsorted[j] < unsorted[j-1]:
				unsorted[j], unsorted[j-1] = unsorted[j-1], unsorted[j]
	
	return unsorted

print insertion_sort([554,3,64,433,223])