from re import sub
from sys import argv

with open(argv[1]) as file:
    data = sub("\W"," ", file.read()).lower().split()

record = {}
for word in data:
    if word in record:
        record[word] += 1
    else:
        record[word] = 1

for top_word, occurance in sorted(record.items(), key=lambda k:k[1], reverse=True)[:10]:
    print "The word \"{0}\" has {1} occurance".format(top_word, occurance)
