#! /usr/bin/python

import sys


for line in sys.stdin:

	line = line.strip()
	tokens = line.split()
	
	if(tokens[0] == 'mark'):
		print("{0}\t{1}\t{2}\t{3}".format(tokens[1],tokens[0],tokens[2],tokens[3]))
	else:
		print("{0}\t{1}\t{2}".format(tokens[1],tokens[0],tokens[2]))
