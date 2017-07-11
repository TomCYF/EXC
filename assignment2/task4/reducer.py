#! /usr/bin/python

import sys

pre_PId = ""
OUId = ""
items = []

for line in sys.stdin:
	items = line.strip().split()
	if len(items) == 1:
		pre_PId = items[0]
	else:
		if pre_PId == items[0]:
			print("{0}\t{1}\t{2}".format(items[1],items[0],1))

if len(items) == 2:
	if pre_PId == items[0]:
		print("{0}\t{1}\t{2}".format(items[1],items[0],1))
