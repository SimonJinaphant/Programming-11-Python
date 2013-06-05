from sys import stdout, argv
from time import sleep

def display_text(message, delay=2, type_delay=0.05):
	for _, letter in enumerate(message):
		#Produce a typing animation effect
		stdout.write(letter)
		stdout.flush()
		sleep(type_delay)
	
	#Pause for the user to read the output, and reset prompt to begining
	sleep(delay)
	stdout.write("\r")
	
	#Erasing the printed text by printing empty spaces fast
	if delay != 0:
		display_text(" "*len(message), 0, 0.01)


with open(argv[1]) as file:
	for lines in file.readlines():
		display_text(lines.strip())
