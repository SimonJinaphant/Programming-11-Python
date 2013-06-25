from sys import argv

with open(argv[1],'r') as f:
	encrypted_data = [encoded.decode('utf-8')[:-1] for encoded in f.readlines()]

uncrypted_data = []
for s, sentence in enumerate(encrypted_data):
	uncrypted_data.append(list())
	for i, letter in enumerate(sentence):
		#print letter
		uncrypted_data[s].append(unichr((ord(letter)-0x4E00)^0x2D))

with open(argv[1],'w') as f2:
	for s1, sen in enumerate(uncrypted_data):
		f2.write(u"".join(sen).encode('utf-8'))
