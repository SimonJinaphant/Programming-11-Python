startingPay = float(raw_input("Enter your starting payment: $"))
daysWorked = int(raw_input("Enter the number of days worked: "))

dayCounter = 0
totalPayment = 0.0

while dayCounter < daysWorked:
	totalPayment+=startingPay
	startingPay*=2
	dayCounter+=1

print totalPayment
