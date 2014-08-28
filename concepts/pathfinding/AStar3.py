import heapq
from sys import argv
from time import sleep

'''
	FASTER than AStar2.py but less accurate at larger path...
	Nodes are stored in a dynamic fashion
'''

class Node:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.g_score = 0

		self.parent = None

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __hash__(self):
		return hash(self.x) ^ hash(self.y)

def display_world():
	for row in world:
		for cell in row:
			print cell,
		print
	

def move_cost(a, b):
	return 14 if a.x == b.x or a.y == b.x else 10



def h_cost(node):
	dx1 = node.x - end.x
	dy1 = node.y - end.y
	dx2 = start.x - end.x
	dy2 = start.y - end.y
	cross = abs(dx1*dy2 - dx2*dy1)

	
	x = abs(node.x - end.x)
	y = abs(node.y - end.y)
	
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
			row.append(cell)
			
			if cell == "S":
				start = Node(x , y)
				
			if cell == "0":
				end = Node(x , y)

path = []
open_set = set()
open_heap = []
closed_set = set()

open_set.add(start)
open_heap.append((0, start))

while open_set:
	current = heapq.heappop(open_heap)[1]
	closed_set.add(current)

	if current == end:
		#print "Done"
		path.append(current)
		while current.parent != None:
			current = current.parent
			path.append(current)

		break

	#world[current.y][current.x] = "+"

	for x in xrange(-1, 2):
		for y in xrange(-1, 2):
			if abs(x) + abs(y) != 0:
				neighbour = Node(current.x + x, current.y + y)

				if world[neighbour.y][neighbour.x] == "X" or neighbour in closed_set:
					continue

				if abs(x) + abs(y) == 2:
					if world[current.y][current.x+x] == "X" or world[current.y+y][current.x] == "X":
						continue

				#world[neighbour.y][neighbour.x] = "#"
				cost = current.g_score + move_cost(current, neighbour)

				if neighbour in open_set and cost < neighbour.g_score:
					heapq.heappop(open_heap)	#??????? POP???
					open_set.remove(neighbour)

				if neighbour not in open_set and neighbour not in closed_set:
					neighbour.g_score = cost
					open_set.add(neighbour)
					heapq.heappush(open_heap, (neighbour.g_score + h_cost(neighbour), neighbour))
					neighbour.parent = current
	#display_world()
	#sleep(0.05)
		#print neighbour.x, neighbour.y, neighbour.g_score, h_cost(neighbour)
	#raw_input(":")

#---------------------------------------------------------------------------------



for step in path[::-1]:
	world[step.y][step.x] = '.'
display_world()
#sleep(0.05)


