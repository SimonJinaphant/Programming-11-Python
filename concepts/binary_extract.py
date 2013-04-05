from math import log

input_A = 0b10001
input_B = 0b101


def get_bit(bit_sequence, bit_position):
	'''
		Returns the bit at the corresponding bit position via bitwise operations
		
		To get the bit we create a bitmask with the testing position being the bit position
		next we shift the results to make sure we only receive the bit we want
	'''
	return (bit_sequence & (1 << bit_position)) >> bit_position



def half_adder(bit_A, bit_B):
	'''
		Returns a tuple containing the sum and carry of the two bits
		
		A half adder works by using the XOR operator on two bits to get the sum
		and an AND operator to determine if there is a carry
		
		A carry happens when both bits are 1
	'''
	return (bit_A ^ bit_B, bit_A & bit_B)
	
	
	
def full_adder(bit_A, bit_B, carry_In = 0):
	'''
		Returns a tuple containing the sum and carry of the bits, including the carry
		
		A full adder is composed of two half adders. 
		
		- One half adder is responsible for finding the sum and carry of the two input 
		bits, in this example it's input_A and input_B
		
		- The second half adder is responsible for finding the sum and carry to the first 
		half adder's sum and the carry_In
		
		- The two half adder's carry is then tested with an OR operator to test if there's
		a carry in this entire addition
		
		A carry happens if all three inputs are 1
	'''

	sum_AB, carry_AB = half_adder(bit_A, bit_B)
	
	sum_total, carry_ABC = half_adder(sum_AB, carry_In)
	
	return (sum_total, carry_AB | carry_ABC)

	
	
def binary_adder(sequence_A, sequence_B):
	'''
		Returns a string with the sum of the two arbitrary size bit sequences
		
		To perform an addition of two binary sequence we use the full adders to add two
		bits at each corresponding bit position
		
		If there's still a carry left from the final operation we append it
		Since we're adding from right to left we need to reverse the sums
	'''
	sequence_sum = []
	carry_in = 0
	
	#The length of a binary sequence is determine by truncating log2(sequence) and adding 1
	for i in xrange(int(log(max(sequence_A, sequence_B), 2)) + 1):
		'''
			Assign @sum to be the first element in the tuple returned from full_adder()
			and reassign @carry_in to the second element
			
			Append the sum as a string type since we're printing out to the screen later
		'''
		sum, carry_in = full_adder(get_bit(sequence_A, i), get_bit(sequence_B, i), carry_in)
		sequence_sum.append(str(sum))
	
	if carry_in & 1 == 1:
		sequence_sum.append('1')
	
	return "".join(sequence_sum[::-1])
		


print binary_adder(input_A, input_B)