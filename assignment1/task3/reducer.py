#! /usr/bin/python

import sys

max_line = 0
max_token = 0
for line in sys.stdin:
	line = line.strip()
	line_number = len(line)
	
	words = line.split()
	for word in words:
		if len(word) > max_token:
			max_token = len(word)	

	if line_number > max_line:
		max_line = line_number
	
print ('{0}\t{1}'.format(max_line, max_token))
	
