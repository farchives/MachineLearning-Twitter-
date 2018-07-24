import numpy as np
import torch
import torch.nn as nn
import re

def textmodif(filename):
	filename = filename
	text = []
	edit = []
	ban = np.array(['https','RT','\\'])
	count = 0

	with open (filename,'r') as inputfile:
		for line in inputfile:
			line = line.strip().split(' ')
			for i in range(0, len(line)-1):
				text.append(line[i])

	textnp = np.array(text)
	textnp.flatten()

	for i in range (0,len(textnp),1):
		temp = textnp[i]
		for x in range(0,len(ban)):
			tempban = ban[x]
			if np.array_equal(temp[0:len(tempban)],tempban[:]):
				#print(temp[0:len(tempban)],tempban[:])
				np.delete(textnp[i],0)
				#print(textnp[i])
				count = count+1
	'''
	for a in range (0,len(textnp),1):
		temp = textnp[a]
		if np.array_equal(temp[0:2],'[b') is False:
			textnp[a] = np.core.defchararray.add(textnp[a],textnp[a+1])
			print(textnp[a])
	'''

	print(count)
	width = textnp.shape[0]
	np.reshape(textnp,(width))
	np.savetxt('new%s' % (filename), textnp, delimiter=" ",fmt = "%s")

	return ('new%s' % filename)