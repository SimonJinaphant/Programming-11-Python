from sys import argv

with open(argv[1],'r') as f:
	data = map(lambda s: [unichr((ord(chr)^0x2D)+0x4E00) for chr in s],
		 f.readlines())

with open(argv[1],'w') as f2:
	for line in data:
		f2.write(u"".join(line).encode('utf8')+"\n")

