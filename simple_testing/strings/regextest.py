import re		#import the regex library

mylist = []		#Create an empty list

input = raw_input("Enter a string: ").strip()

for i in input:
	if re.search("[A-Za-z]",i) != None:		
		#If an element in the list contains a character from A to Z and a to z...
		print "\tYour input contains a letter...bad..."
		continue;
	else:
		mylist.append(int(i))
		print "\t", mylist
		
print "\n\n\nYour list is", mylist