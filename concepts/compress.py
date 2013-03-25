def compress(uncompressed):
	uncompressed.append(None)	#Append for including last group
	groups = []
	
	current_type = type(uncompressed[0])
	start = 0
	
	for i in xrange(1, len(uncompressed)):
		if type(uncompressed[i]) != current_type:
			if current_type == type("str"):
				groups.append("".join(uncompressed[start:i]))
			else:
				groups.extend(uncompressed[start:i])
				
			start = i
			current_type = type(uncompressed[i])
	
	return groups

	
print compress(['Hello ', 'world', ' is ', 'unoriginal', 54, 647, 'lolz', 'derp', 32])
print compress(['hello ', 'world', '!', 17, 12, 'foo'])