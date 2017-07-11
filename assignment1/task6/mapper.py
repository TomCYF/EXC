#! /usr/bin/python

import sys

cur_context = ""
context = {}
num = 0
count = {}
for line in sys.stdin:
	
	tokens = line.strip().split()
	
	if(tokens[0:2] == cur_context):
		count[tokens[2]] = int(tokens[3])
	else:
		if cur_context:
			print("{0} {1} {2}".format(cur_context[0],cur_context[1],count))
		cur_context = tokens[0:2]
		count = {}
		count[tokens[2]] = int(tokens[3])

if cur_context:
	print("{0} {1} {2}".format(cur_context[0],cur_context[1],count))
