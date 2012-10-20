init_payment = int(raw_input("Enter your initial payment in cents: "))
daysWorked = int(raw_input("How many days are you working?: "))

print "You'll earn: $",((init_payment << daysWorked)-init_payment)/100.0