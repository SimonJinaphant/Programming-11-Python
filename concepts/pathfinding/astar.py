#from Queue import PriorityQueue as PQueue
from datastructure import PriorityQueue as PQueue
from sys import argv

class Node:
	def __init__(self, x, y, g_score, h_score, parent=None):
		self.x = x
		self.y = y
		self.g_score = g_score
		self.h_score = h_score
		self.parent = parent

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __str__(self):
		return "({0}, {1}, G:{2}, H:{3})".format(self.x, self.y, self.g_score, self.h_score)

	def __repr__(self):
		return self.__str__()


def display_world():
	for row in world:
		print " ".join(row)

def adjacent_to(node):
	for _x in xrange(-1, 2):
		for _y in xrange(-1, 2):
			if abs(_x) ^ abs(_y) != 0:
				#if abs(_x) ^ abs(_y):
				yield Node(node.x+_x, node.y+_y, node.g_score + 10, h_score(node, end), node)
				#else:
				#	yield Node(node.x+_x, node.y+_y, node.g_score + 14, h_score(node, end))

def h_score(a, b):
	return abs(a.x - b.x) + abs(a.y - b.y)

with open(argv[1], 'r') as map_data:
	world = []
	start = None
	end = None

	for x, row in enumerate(map_data.readlines()):
		world_row = []
		for y, cell in enumerate(row.strip().replace(" ", "")):
			if cell == "S":
				start = Node(x, y, 0, 0)

			if cell == "0":
				end = Node(x, y, 0, 0)

			world_row.append(cell)

		world.append(world_row)

open_nodes = PQueue()
open_nodes.enqueue(start)
closed_nodes = []

'''for row in world:
	print " ".join(row)'''


#print "Start:", start
path = []
while open_nodes.size != 0:
	current_node = open_nodes.dequeue()
	#print "Analysing:", current_node
	if current_node == end:
		#print "Done!"
		
		
		#print current_node.parent
		while current_node != start:
			path.append(current_node)
			current_node = current_node.parent
		path.append(start)
		#print path[::-1]
		break
		#Trace back path

	if not current_node in closed_nodes:
		closed_nodes.append(current_node)

	for cell in adjacent_to(current_node):
		
		if world[cell.x][cell.y] == "X" or cell in closed_nodes:
			continue
		#print "\t",cell

		cost = current_node.g_score + h_score(current_node,cell)
		if not open_nodes.contains(cell):
				#print "\tAdding", cell, "to open_nodes"
				open_nodes.enqueue(cell)

		else:
			#print "\tShould I replace", cell
			nc = open_nodes.get(cell)
			if nc.g_score > cost:
				#print "\tReplacing", cell
			
				nc.parent = current_node
				nc.g = cost

				open_nodes.readjust(nc)
		#raw_input(":")
	#print closed_nodes
	#raw_input()


'''for step in path:
	world[step.x][step.y] = '.'

display_world()
'''
