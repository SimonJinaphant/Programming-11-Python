import math

start = int(raw_input("Enter a starting range: "))
finish = int(raw_input("Enter a finishing range: "))

numSum = 0
numList = range(start,finish+1)
listLength = len(numList)
unpairedNumber = 0;

if ((listLength & 1)==1):
	unpairedNumber = numList[int(math.floor(listLength/2))]

numSum = (numList[0]+numList[-1])*math.floor(listLength/2)+unpairedNumber

print numSum


