from sys import argv

with open(argv[1],'r') as f:
    for i in xrange(int(argv[2])):
            print f.readline(),