from sys import argv
from re import sub
from math import ceil

with open(argv[2],'r') as f:
    content = sub('\n','',f.read())
    
for line in xrange(0, int(ceil(len(content)/float(argv[1]))), int(argv[1])):
	print content[line:line+int(argv[1])]
		
