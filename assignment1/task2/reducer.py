#! /usr/bin/python

import sys

pre_line = ""
total_exist = 0
for line in sys.stdin:
	line = line.strip()	
	cur_line, exist = line.split("\t",1)
	exist = int(exist)

	if pre_line == cur_line:
		total_exist += 1
	else:
		if total_exist > 0:	
			pre_line = cur_line
			total_exist = 0
		else:
			if pre_line:
				print("{0}".format(pre_line))
				total_exist = 0
	
	pre_line = cur_line

if total_exist == 0:
	print("{0}".format(pre_line))
			
				


		
