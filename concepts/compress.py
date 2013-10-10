def compress(uncompressed):
	uncompressed.append(None)	#Append for including last group
	groups = []
	
	current_type = type(uncompressed[0])
	start = 0
	
	for i in xrange(1, len(uncompressed)):
		if type(uncompressed[i]) != current_type:
			if current_type == type("string"):
				print "String"
				groups.append("".join(uncompressed[start:i]))
			elif current_type == type(1):
				print "Int"
				groups.append(sum(uncompressed[start:i]))
			else:
				print "Nope"
				groups.extend(uncompressed[start:i])
				
			start = i
			current_type = type(uncompressed[i])
	
	return groups

	
print compress(['Hello ', 'world', ' is ', 'unoriginal', 54, 647, 'lolz', 'derp', 32])
print compress(['hello ', 'world', '!', 17, 12, 'foo'])