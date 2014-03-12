from Queue import PriorityQueue as PQueue
from collections import Counter

class Node:
	def __init__(self, text, score, leftChild=None, rightChild=None):
		self.text = text
		self.score = score
		
		self.leftChild = leftChild
		self.rightChild = rightChild

	def __lt__(self, n):
		return n.score > self.score

	def __str__(self):
		return "({0}, {1})".format(self.text, self.score)

table = {}
def traverse(node, path):
	if len(node.text) == 1:
		#Base case -> Found a single letter!
		table[node.text] = path
	
	#Traverse each branch if it exists, remembering to record our path down
	if node.leftChild != None:
		np =  path[:]+'0'
		traverse(node.leftChild, np)
	
	if node.rightChild != None:
		np =  path[:]+'1'
		traverse(node.rightChild, np)


uncompressed = "mississippi river"

#Create nodes for every letter in the uncompressed sentence
'''
	I used a Priority Queue to ensure that the smallest valued node are always the root.
	Removing the smallest node will be quicker, compare to searching for the smallest.
	The Priority Queue will internally re-adjust itself if needed.
'''

nodes = PQueue()
for letter, base_score in Counter(uncompressed).items():
	nodes.put(Node(letter, base_score))

#Build-up the Binary Tree
while nodes.qsize() != 1:
	left = nodes.get()
	right = nodes.get()

	nodes.put(Node(left.text+right.text, left.score+right.score, left, right))

#Traverse the binary tree in a depth-first-search style in order to determine the path to every single letter node
traverse(nodes.get(), '')

compressed = uncompressed[:]
for letter, path in table.items():
	print "'{0}' -> {1}".format(letter, path)
	compressed = compressed.replace(letter, path)


print compressed
print len(compressed), "bits"