

"""
 13.1    Word frequency analysis
"""


import os 
import string

def cleanFile(fname):
	fin = open(curr_file)

	res = []

	for line in fin:
		words = line.split()
		for word in words:
			s = word.translate(string.maketrans("", ""), string.punctuation + string.digits)
		res.append(s.strip().lower())

	return res 


