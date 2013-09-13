from abstractDataStructure import AbstractStack
from structureNode import LinkedNode

class Stack(AbstractStack):

	class StackIterator():
		def __init__(self, start):
			self.node = start

		def __iter__(self):
			return self
		
		def next(self):
			if self.node == None:
				raise StopIteration
			else:
				prev = self.node
				self.node = self.node.getNext()
				return prev.getData()

		
	def __init__(self, *args):
		self.head = None
		self.size = 0
		
		if len(args) > 0:
			for item in args:
				self.push(item)


	def push(self, item):
		'''
			Add a node to the stack and pushed the remaining nodes down the stack
			Complexity: O(1)
		'''
		temp = LinkedNode(item)
		temp.setNext(self.head)
		self.head = temp
		
		self.size += 1
		
	
	def pop(self):
		'''
			Returns the head item of the stack and remove it
			Complexity: O(1)
		'''
		current = self.head
		if current != None:
			self.head = current.getNext()
		
		self.size -= 1
		
		return current
	

	def peek(self):
		'''
			Returns the head item of the stack but doesn't remove it
			Complexity: O(1)
		'''
		return self.head


	def isEmpty(self):
		'''
			Determines if the stack is empty
			Complexity: O(1)
		'''
		return self.head == None


	def getSize(self):
		'''
			Determines the size of the stack
			Complexity: O(1)
		'''
		return self.size
	

	def getValue(self, index):
		'''
			Returns the value of the node with the corresponding index
			Complexity: O(n)
		'''
		currentIndex = 0	
		for element in Stack.StackIterator(self.head):
			if currentIndex == index:
				return element
				
			currentIndex += 1
		
	
	def __iter__(self):
		'''
			Returns an stack iterator object
			Complexity: O(1)
		'''
		return Stack.StackIterator(self.head)
	
stack = Stack('A', 'B', 'C', 'D', 'E')
stack.push('F')
stack.push('G')
stack.pop()

print "\n\n"
for i in stack:
	print i

print stack.getSize()
print stack.getValue(1)
