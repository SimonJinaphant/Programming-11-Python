def merge(left_list, right_list):
	sorted_list = []
	
	'''
		While one of the list is not empty:
			Compare each head element in the list
			Remove the lowest element compared and add it to end of the sorted_list
			
		We add the lowest to the end because the sorted_list is in a stack (F.I.L.O.) format
		By continuously adding lower valued items to the end we know that the item added
		after will be greater since it wasn't added before
		
		Therefore, in the end we can guarantee that the first item will be the lowest of
		all the items and the last item will be the greatest
	'''
	while len(left_list) != 0 and len(right_list) != 0:
		if left_list[0] < right_list[0]:
			sorted_list.append(left_list.pop(0))
		else:
			sorted_list.append(right_list.pop(0))
			
	'''
		Add any left-over elements to the end of the list, due to the logic of merge sort,
		if there are left-over elements it will always be the largest element(s)
	'''
	if len(left_list) != 0:
		sorted_list.extend(left_list)
	if len(right_list) != 0:
		sorted_list.extend(right_list)
	
	return sorted_list

def merge_sort(unsorted):
	'''
		Divide the list into two and, and keep doing it until it's only a 
		list with only one element inside
		
		then call merge() to compare the values in each list, eventually
		re-growing the list into it's original size
	'''
	if len(unsorted) == 1:
		return unsorted
	
	left_list = unsorted[:len(unsorted)/2]
	right_list = unsorted[len(unsorted)/2:]
	
	return merge(merge_sort(left_list), merge_sort(right_list))
	
print merge_sort([504, 504, 68, 14, 64, 45, 101, 303])