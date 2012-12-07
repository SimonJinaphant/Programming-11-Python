"""
	Lists are mutable objects, so we can simple set the contents to it's new value directly
	
	Replaces any 4 letter substring with ****
	
"""

words = raw_input("Enter a sentence:").split()

for i in range(len(words)):
	if len(words[i]) == 4:
		words[i] = "****"

print " ".join(words)
