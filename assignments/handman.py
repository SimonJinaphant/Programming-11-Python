message = "singleton"
hint = "Name of a design pattern use to ensure an object is instantiated only once"

display = ['_']*len(message)
errorCounter = 0

def findPosition(guess):
	if guess in message:
		for letter in set(guess):
			for v,k in enumerate(message):
				if message[v] == letter:
					display[v] = letter
		return True
	
	return False	

print '''
-----------Hangman game----------
You can enter a single letter, or a string if you're feeling lucky

Your hint for the secret message is: 
{0}
-----------Hangman game----------
'''.format(hint)


while "".join(display) != message and errorCounter < 10:
	
	userInput = raw_input("Enter a guess (char or string type): ").lower()

	if not findPosition(userInput):
		print "Nope {0} isn't a match to anything... you've got {1} chances left".format(userInput,9-errorCounter)
        	errorCounter += 1
       
	print " ".join(display), "\n\n"
	
print "The game is now over"