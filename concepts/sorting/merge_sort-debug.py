'''
	Merge sort text-debug-visual version
	Highly suggest running this instead of trying to read it, makes more sense in run-time
	
	Used for exploring how merge sort works by printing it's process in every action
'''

def merge(left_list, right_list, depth):
	sorted_list = []
	
	tab_space = '\t' * depth	#Used for showing recursion depth, not part of the algorithm
	
	print tab_space + '---Before sorting----'
	print tab_space + 'Left list contains:', left_list
	print tab_space + 'Right list contains:', right_list
	
	
	print tab_space + '---While sorting---'
	while len(left_list) != 0 and len(right_list) != 0:
		'''
			While one of the list is not empty:
				Compare each head element in the list
				Remove the lowest element compared and add it to end the sorted_list
		'''
		
		print tab_space + 'Current sorted list:', sorted_list
		print tab_space + 'Current left list:', left_list
		print tab_space + 'Current right list:',right_list
	
		if left_list[0] < right_list[0]:
			print tab_space + '{0} is less than {1}: adding {0} to the stack\n'.format(left_list[0], right_list[0])
			sorted_list.append(left_list.pop(0))
			
		else:
			print tab_space + '{0} is greater than or equal to {1}: adding {1} to the stack\n'.format(left_list[0], right_list[0])
			sorted_list.append(right_list.pop(0))
			
	'''
		Add any left-over elements to the end of the list, due to the logic of merge sort,
		if there are left-over elements it will always be the largest element(s)
	'''
	print tab_space + '---After sorting---'
	if len(left_list) != 0:
		print tab_space + '{0} is left-over: adding all to the end'.format(left_list)
		sorted_list.extend(left_list)
	if len(right_list) != 0:
		print tab_space + '{0} is left-over: adding all to the end'.format(right_list)
		sorted_list.extend(right_list)
		
	
	print tab_space + '---Returning---'
	print tab_space + 'Returning sorted list: {0} \n\n'.format(sorted_list)
	
	return sorted_list


def merge_sort(unsorted, depth):
	'''
		Divide the list into two and, and keep doing it until it's only a 
		list with only one element inside
		
		Then call merge() to compare the values in each list, eventually
		re-growing the list into it's original size
		
		This is a depth first recursive transversal
	'''
	
	if len(unsorted) == 1:
		return unsorted
	
	left_list = unsorted[:len(unsorted)/2]
	right_list = unsorted[len(unsorted)/2:]
	
	return merge(merge_sort(left_list, depth+1), merge_sort(right_list, depth+1), depth)

	
print 'Final sorted list: {0}'.format(merge_sort([504,504,68,14,64,45,101,303], 0))