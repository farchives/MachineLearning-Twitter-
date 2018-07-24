import numpy as np

text = []
edit = []
ban = ["https", "RT","\\"]

with open ('tweets2.txt','r') as inputfile:
	for line in inputfile:
		line = line.strip().split(' ')
		for i in range(0, len(line)-1):
			text.append(line[i])

textnp = np.array(text)
textnp.flatten()

for i in range (0,len(textnp)):
	temp = textnp[i]
	for x in range(0,len(ban)-1):
		for word in temp:
			if word.startswith(ban[x]):
				np.delete(word)

width = textnp.shape[0]
np.reshape(textnp,(width))
np.savetxt('tweets.txt', textnp, delimiter=" ",fmt = "%s")
