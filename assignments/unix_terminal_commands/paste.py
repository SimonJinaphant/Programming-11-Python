from sys import argv

with open(argv[1],'r') as f:
    with open(argv[2],'r') as f2:
        for line, line2 in zip(f.readlines(),f2.readlines()):
            print "{0}\t{1}".format(line.strip(),line2.strip())