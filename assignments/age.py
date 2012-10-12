input = int(raw_input("Hello, how old are you? "))

if input > 100:
	print "You can't purchase alcohol when you're dead ._."
elif input <= 0:
	print "You can't purchase alcohol when you haven't been born yet"
elif input >= 19:
	print "You are old enough to buy alcohol"
else:
	print "Sorry, you are too young"

