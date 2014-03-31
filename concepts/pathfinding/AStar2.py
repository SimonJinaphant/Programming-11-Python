from priority_queue import PriorityQueue as PQueue
from sys import argv

'''
	ACCURATE than AStar3.py but a bit slower
	Nodes are stored in a fixed size manner
'''

class Node:
	def __init__(self, symbol, x, y):
		self.symbol = symbol
		self.x = x
		self.y = y
		self.g_score = 0
		self.h_score = 0
		self.visited = False
		self.closed = False
		self.parent = None

	def __lt__(self, c):
		return self.g_score + self.h_score < c.g_score + c.h_score

	def __str__(self):
		return self.symbol

	def __repr__(self):
		return self.__str__()

	def info(self):
		return "({0},{1}) -> H:{2}, G:{3}".format(self.x, self.y, self.h_score, self.g_score)

def display_world():
	for row in world:
		for cell in row:
			print cell,
		print


def h_score(a, b):
	dx1 = a.x - b.x
	dy1 = a.y - b.y
	dx2 = start.x - b.x
	dy2 = start.y - b.y
	cross = abs(dx1*dy2 - dx2*dy1)
	
	x = abs(a.x - b.x)
	y = abs(a.y - b.y)
	if x > y:
		return (14*y + 10*(x-y)) + cross*0.001
	else:
		return (14*x + 10*(y-x)) + cross*0.001



with open(argv[1], 'r') as map_data:
	world = []
	start = None
	end = None

	for y, map_row in enumerate(map_data.readlines()):
		row = []
		world.append(row)
		for x, cell in enumerate(map_row.strip().replace(" ", "")):
			n = Node(cell, x , y)
			row.append(n)
			if cell == "S":
				start = n
				
			if cell == "0":
				end = n

path = []
open_nodes = PQueue()
open_nodes.enqueue(start)

#---------------------------------------------------------------------------------

while open_nodes:
	current = open_nodes.dequeue()

	if current == end:
		print "Done!"
		
		while current != None:
			path.append(current)
			current = current.parent
			
		break

	current.closed = True
	current.symbol = "+"

	for _x in xrange(-1, 2):
		for _y in xrange(-1, 2):
			if abs(_x) + abs(_y) != 0:

				neighbor = world[current.y+_y][current.x+_x]

				if neighbor.closed or neighbor.symbol == "X":
					continue

				if abs(_x) + abs(_y) == 2:
					#If neighbouring tile is a diagonal tile, check to see if diagonal movement will cut corners...
					if world[current.y][current.x+_x].symbol == "X" or world[current.y+_y][current.x].symbol == "X":
						continue

				neighbor.symbol = "#"
				g = current.g_score + (14 if abs(_x) + abs(_y) == 2 else 10)
				V = neighbor.visited

				if not V or g < neighbor.g_score:
					neighbor.visited = True
					neighbor.parent = current
					neighbor.h_score = h_score(neighbor, end)
					neighbor.g_score = g

					if not V:
						open_nodes.enqueue(neighbor)
					else:
						open_nodes.readjust(neighbor)


	#print neighbor.info()
	#display_world()
	#raw_input(":")


for step in path[::-1]:
	world[step.y][step.x].symbol = '.'
display_world()


