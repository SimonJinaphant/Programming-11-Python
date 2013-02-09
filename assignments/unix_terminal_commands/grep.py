from sys import argv

with open(argv[2],'r') as f:
   for line in f.readlines():
        if argv[1] in line:
            print line,