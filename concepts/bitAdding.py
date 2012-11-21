def halfAdder(aIn, bIn):
	return (aIn ^ bIn, aIn & bIn)
	
	
def fullAdder(aIn,bIn,cIn):
	
	sumAB = halfAdder(aIn,bIn)
	sumTotal = halfAdder(sumAB[0],cIn)

	return (sumTotal[0], sumTotal[1] | sumAB[1])
	
	
def eightBitAdder(byteA, byteB, debug=False):
	if debug:
		print "Input byte A:", byteA
		print "Input byte B", byteB,"\n"
	
	cIn = 0
	output = []
	
	for bit in range(7,-1,-1):
		
		result = fullAdder(byteA[bit],byteB[bit],cIn)
		
		if debug:
			print "Bit index:",bit
			print "Bit A:",byteA[bit],"\t Bit B:",byteB[bit],"\t Carry In:",cIn
			print "Sum of bits:",result[0],"\t Carry out:",result[1],"\n\n"
		
		cIn = result[1]
		output.append(result[0])
	

	if cIn == 1:
		output.append(cIn)
	
	return output[::-1]
		

byte1 = [0,1,0,0,1,0,1,0]
byte2 = [1,1,0,0,0,1,1,1]

print eightBitAdder(byte1, byte2, True)