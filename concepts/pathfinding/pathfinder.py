from sys import argv
from Queue import Queue
from copy import deepcopy

class Coordinate:
	def __init__(self, x, y, counter):
		self.x = x
		self.y = y
		self.counter = counter

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		return "({0}, {1}, {2})".format(self.x, self.y ,self.counter)

	def release(self):
		#A simple way to unpack a Coordinate's values
		return (self.x, self.y, self.counter)


class PathFinder:
	def __init__(self, path_to_file):

		with open(path_to_file, 'r') as grid_file:
			self.world = [[cell for cell in row.strip().replace(" ", "").replace("_"," ")] for row in grid_file.readlines()]

		self.path = [(cell.x, cell.y) for cell in self._generate_path()]
		
		
	def _is_valid(self, coordinate):
		return coordinate.x >= 0 and coordinate.x < len(self.world[0]) and coordinate.y >= 0 and coordinate.y < len(self.world) and self.world[coordinate.y][coordinate.x] != 'X'
	

	def display_world(self):
		for row in self.world:
			print " ".join(row)


	def _generate_path(self):

		def should_replace(coordinate):
			cell = closed_grid[coordinate.y][coordinate.x]
			return (isinstance(cell, Coordinate) and cell.counter > coordinate.counter) or isinstance(cell, basestring)
		
		def find_start():
			#Set up main list of coordinates
			open_list = Queue()
			open_list.put(end)
			
			#Find the starting point and calculate the distance taken
			while open_list.qsize() != 0:
				root = open_list.get()

				if self.world[root.y][root.x] == "S":
					#We've found the starting point!
					return root
					
				closed_grid[root.y][root.x] = root
				cx, cy, cc = root.release()

				for y in xrange(cy-1, cy+2):
					for x in xrange(cx-1, cx+2):
						if (x-cx) * (y-cy) == 0:		#A trick to only get adjacent cells in a compass (NESW) style 
							new_coord = Coordinate(x,y,cc+1)
							if self._is_valid(new_coord) and should_replace(new_coord):
								closed_grid[new_coord.y][new_coord.x] = new_coord
								open_list.put(new_coord)

		def trace_path():
			current = find_start()
			assert current != None
			path = []

			while True:
				cx, cy, cc = current.release()
				path.append(current)

				if closed_grid[cy][cx] == end:
					return path

				for y in xrange(cy-1, cy+2):
					for x in xrange(cx-1, cx+2):
						if (x-cx) * (y-cy) == 0 and isinstance(closed_grid[y][x], Coordinate) and closed_grid[y][x].counter == cc - 1:
							current = Coordinate(x, y, cc-1)

		#Find the ending point
		for y, row in enumerate(self.world):
			for x, cell in enumerate(row):
				if cell == "0":
					end = Coordinate(x, y, 0)

		closed_grid = deepcopy(self.world)
		return trace_path()



myWorld = PathFinder(argv[1])
'''
for step in myWorld.path:
	myWorld.world[step[1]][step[0]] = '.'

myWorld.display_world()'''