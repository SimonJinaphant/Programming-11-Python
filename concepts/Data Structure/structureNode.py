class LinkedNode:
	
	def __init__(self, data, next=None):
		self.data = data
		self.next = next
	
	def setNext(self, next):
		self.next = next	
	
	def getNext(self):
		return self.next
		
	def setData(self, data):
		self.data = data
	
	def getData(self):
		return self.data
		
	def __str__(self):	
		return "LinkedNode %s: %s" % (id(self), str(self.data))


		
class DoubleLinkedNode(LinkedNode):

	def __init__(self, data, next=None, previous=None):
		self.data = data
		self.next = next
		self.previous = previous
		
	def setPrev(self, node):
		self.previous = node
		
	def getPrev(self):
		return self.previous
		
	def __str__(self):	
		return "DoubleLinkedNode %s: %s" % (id(self), str(self.data))