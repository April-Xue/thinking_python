

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


