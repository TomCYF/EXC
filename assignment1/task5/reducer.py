#! /usr/bin/python

import sys

i = 0
for line in sys.stdin:
	line = line.strip()
	
	if i<20:
		print(line)

	i += 1
	
