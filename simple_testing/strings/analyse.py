vowels = ['A','E','I','O','U']

inputRaw = raw_input("Enter a string: ")


def vowelCount(letter):
	for vowelLetter in vowels:
		if letter == vowelLetter or letter == chr(ord(vowelLetter)+0x20):
			print letter, "is a vowel"
			
def analyseString(inputString):			
	prevLetter = ''
	wordCount = 0

	for i in range(0,len(inputString)):
		vowelCount(inputString[i])
	
		if (inputString[i] == ' ' and prevLetter != ' ') or i == len(inputString)-1:
			wordCount+=1

		prevLetter = inputString[i]
		
	print "There are", wordCount, "words in total"

analyseString(inputRaw)
