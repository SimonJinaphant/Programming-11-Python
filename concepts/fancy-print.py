from sys import stdout, argv
from time import sleep

def fancy_print(message, life_time=2, type_delay=0.05):
	'''
		Prints out the message with a typing style effect

		@param message = The message you want to print
		@param life_time = The duration the entire message stays on the screen after it's printed
		@param type_delay = The delay in the typing effect speed
	'''
	for letter in message:
		stdout.write(letter)
		stdout.flush()
		sleep(type_delay)

	sleep(life_time)
	stdout.write("\r")
	
    #A cheap but easy way to "erase" the text previously printed...
	if life_time != 0:
		fancy_print(" "*len(message), 0, 0.01)


'''
	Tip #1
	Whenever you don't understand something: try to change it
	or remove it and see how it effects the program when it runs

	Tip #2
	If you're confuse about the flow of the program when it runs:
	place a couple of print statements to give yourself a nice reference point

	Tip #3
	If you seriously don't understand something: Google it! there's no shame :)
'''

with open(argv[1]) as file:
	for lines in file.readlines():
		fancy_print(lines.strip())