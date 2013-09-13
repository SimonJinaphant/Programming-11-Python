class AbstractStructure():

	def isEmpty(self):
		return NotImplemented
		
	def getSize(self):
		return NotImplemented



class AbstractStack(AbstractStructure):

	def push(self):
		return NotImplemented

	def pop(self):
		return NotImplemented
		
	def peek(self):
		return NotImplemented



class AbstractQueue(AbstractStructure):

	def enqueue(self, element):
		return NotImplemented
		
	def dequeue(self):
		return NotImplemented



class AbstractDeque(AbstractStructure):

	def addFront(self, element):
		return NotImplemented
	
	def addRear(self, element):
		return NotImplemented
		
	def removeFront(self):
		return NotImplemented
		
	def removeRear(self):
		return NotImplemented