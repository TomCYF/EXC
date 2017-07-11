#! /usr/bin/python

import sys

num = 0
seq = ""

for line in sys.stdin:
	line = line.strip()
	seq, num = line.split("\t",1)
	
	print("{0}\t{1}".format(num,seq))
