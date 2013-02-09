from sys import argv

with open(argv[1],'r') as f:
    for line in f.readlines()[::-1]:
            print line,