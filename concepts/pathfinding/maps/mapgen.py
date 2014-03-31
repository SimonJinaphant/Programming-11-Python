from random import randrange

scale = 80

world = []
world.append(['X'*(scale+2)])
for y in xrange(scale):
	row = ['X']

	for x in xrange(scale):
		if randrange(0,3) == 5:
			row.append("X")
		else:
			row.append("_")
	row.append('X')
	world.append(row)

world.append(['X'*(scale+2)])

with open("bigmap4.txt", 'w') as out:
	for row in world:
		out.write("".join(row)+'\n')
