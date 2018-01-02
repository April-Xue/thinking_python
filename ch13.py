

"""
 13.1    Word frequency analysis
"""


import os 
import string

def cleanFile(fname):
	fin = open(fname)

	res = []

	for line in fin:
		words = line.split()
		for word in words:
			s = word.translate(string.maketrans("", ""), string.punctuation + string.digits)
		res.append(s.strip().lower())

	return res 

#print len(cleanFile('../words.txt'))
#print cleanFile('../words.txt')[:100]


def processLine(line):

	words = line.split()
	res = []

	for word in words:
		s = word.translate(string.maketrans("", ""), string.punctuation+string.digits)
		res.append(s.strip().lower())

	return res 

def processFile(fname, processLine):

	d = dict()
	with open(fname) as fin:
		for line in fin:
			lst = processLine(line)
			for word in lst:
				d[word] = d.get(word, 0) + 1

	return d 





