from math import log10

#Not working for uneven length numbers :(

def karatsuba(num_1, num_2, depth):
	if num_1 < 10 or num_2 < 10:
		print ("\t"*depth) + "Base case", num_1 * num_2, "\n"
		return num_1 * num_2
		
	length = int(log10(max(num_1, num_2)))+1
	print ("\t"*depth) + "Max length:", length
	
	high_1, low_1 = divmod(num_1, 10**(length/2))
	high_2, low_2 = divmod(num_2, 10**(length/2))
	
	print ("\t"*depth) + "Spliting:"
	print ("\t"*depth) + "{0} --> (A){1}, (B){2}".format(num_1, high_1, low_1)
	print ("\t"*depth) + "{0} --> (C){1}, (D){2}".format(num_2, high_2, low_2)
	
	#NOT AD_BC...
	ac = karatsuba(high_1, high_2, depth+1)
	total = karatsuba((high_1+low_1),(high_2+low_2), depth+1)
	bd = karatsuba(low_1, low_2, depth+1)
	
	print ("\t"*depth) + "AC = {0}, AD+BC = {1}, BD = {2}".format(ac,total-bd-ac, bd)
	
	result = (ac*10**length) + (total-bd-ac)*10**(length/2) + bd
	print ("\t"*depth), result, "\n\n"
	return result



print karatsuba(1234,5678,0)