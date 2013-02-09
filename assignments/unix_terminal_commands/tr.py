from sys import argv
from re import sub

with open(argv[3],'r') as f:
   for line in f.readlines():
        if argv[1] in line:
            print sub(argv[1],argv[2],line),