vowels = ['A','E','I','O','U']
vowelCount = 0

inputRaw = raw_input("Enter a string: ")

for letter in inputRaw:
	for vowel in vowels:
		if letter == vowel or letter == chr(ord(vowel)+0x20):
			print letter, "is a vowel"
			vowelCount+=1
			
print "There are", vowelCount, "vowels in total"