items = [(5,3),(3,2),(4,1)]		#Key = Cost, Value = Profit
capacity = 5

def print_table(table):
	for row in table:
		print row

value_table = [list(None for k in xrange(capacity)) for i in xrange(len(items)+1)]
keep_table = [list(None for k in xrange(capacity)) for i in xrange(len(items)+1)]

for zeros in xrange(capacity):
	keep_table[0][zeros] = value_table[0][zeros] = 0


for i in xrange(1, len(items)+1):
	value, weight = items[i - 1]
	
	for current_capacity in xrange(capacity):
		if weight <= current_capacity + 1:
			above = value_table[i-1][current_capacity]
			max_current = value + value_table[i-1][max(current_capacity-weight, 0)]
			
			if above >= max_current:
				value_table[i][current_capacity] = above
				keep_table[i][current_capacity] = 0
			else:
				value_table[i][current_capacity] = max_current
				keep_table[i][current_capacity] = 1
				
		else:
			keep_table[i][current_capacity] = value_table[i][current_capacity] = 0


#TODO Not working properly...
keep_items = []
remaining_weight = capacity
items_left = len(items)

for kc, kv in items[::-1]:
	if keep_table[items_left][remaining_weight-1] == 0:
		print items_left, remaining_weight-1
		keep_items.append((kc,kv))
	else:
		remaining_weight -= kc
	
	items_left -= 1
			
	
print_table(value_table)

print '\n'

print_table(keep_table)
print keep_items, remaining_weight, items_left