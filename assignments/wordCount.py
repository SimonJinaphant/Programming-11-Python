sen = "hi    mom   by  mom "
words = 0
prev = 0

for let in sen:
		
	if let == ' ' and prev != " ":
		words +=1

	prev = let

print words
