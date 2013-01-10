'''
	A binary addition and subtraction simulator
	
	- Simon Jinaphant
'''


def halfAdder(aIn, bIn):
	'''
		Represents a half adder, given input A and B
		
		@return	return a tuple containing the sum of the two bits and the carried bit
	'''
	return (aIn ^ bIn, aIn & bIn)
	
	
def fullAdder(aIn,bIn,cIn):
	'''
		Represents a full adder, given input A,B, and the carried in C,
		This differs from a half adder which can only add two bits but not 3 bits,
		the third bit being a carried in bit
		 
		@return	returns a tuple containing the sum of the two bits and the carried bit
	'''
	
	sumAB = halfAdder(aIn,bIn)
	sumTotal = halfAdder(sumAB[0],cIn)

	return (sumTotal[0], sumTotal[1] | sumAB[1])
	
def invertBits(bits):
	'''
		Inverts the given bit value by performing a bitwise XOR operation of 1 on each bit
		Uses python list comprehension for shortening the return statement
	'''
	return [bits[i]^1 for i in range(len(bits))]
	
def bitAdder(bitsA,bitsB,debug=False):
	'''
		A generic adder that can be used for not only addition of bits,
		but also part of subtraction
		
		@return	returns a tuple containing the added bits along with a possible carried bit
				which can be used for determining overflow/underflow with bit subtraction
	'''
	if debug:
		print "Input byte A:", bitsA
		print "Input byte B", bitsB,"\n"
		
	cIn = 0
	output = []
	
	for bit in range(7,-1,-1):
		
		result = fullAdder(bitsA[bit],bitsB[bit],cIn)
		
		if debug:
			print "Bit index:",bit
			print "Bit A:",bitsA[bit],"\t Bit B:",bitsB[bit],"\t Carry In:",cIn
			print "Sum of bits:",result[0],"\t Carry out:",result[1],"\n\n"
		
		cIn = result[1]
		output.append(result[0])
	
	return (output[::-1],cIn)


def eightBitAddition(byteA, byteB, debug=False):

	preResults = bitAdder(byteA,byteB,debug)
	
	if preResults[1] == 1:
		print "Appending the carried 1"
		preResults[0].insert(0,1)

	return preResults[0]
	
def eightBitSubtraction(byteA,byteB, debug=False):

	preResults = bitAdder(byteA, invertBits(byteB),debug)
	
	if preResults[1] == 1:
		print "The result is a positive number"
		return bitAdder(preResults[0],[0,0,0,0,0,0,0,1])[0]
		
	print "The result is a negative number"
	return invertBits(preResults[0])

print eightBitAddition([0,1,1,0,1,0,0,1],[0,0,0,0,1,1,0,1])