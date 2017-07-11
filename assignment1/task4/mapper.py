#! /usr/bin/python

import sys

for line in sys.stdin:
	
	line = line.strip()
	tokens = line.split()
	
	for i in range(0,len(tokens)-2):
		print ('{0} {1} {2}\t{3}'.format(tokens[i],tokens[i+1],tokens[i+2],1))
