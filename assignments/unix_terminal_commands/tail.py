from sys import argv

with open(argv[1],'r') as f:
    for line in f.readlines()[::-1][:int(argv[2])]:
            print line,