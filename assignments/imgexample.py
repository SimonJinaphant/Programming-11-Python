import Image, sys

img = Image.open(sys.argv[1],'r')
width, height = img.size

width = int(120.0/height*width) * 2

img = img.resize((width, 120), Image.BILINEAR)
img = img.convert('L')

scale = ['@', '#', 'A', '%', 'S', '<', '*', '+', ':', '.']

with open(sys.argv[2], 'w') as f:
	for y in xrange(120):
		for x in xrange(width):
			lum = img.getpixel((x,y))
			step = int(256/(len(scale)-1))
			index = lum // step
			f.write(scale[index])
		f.write('\n')
