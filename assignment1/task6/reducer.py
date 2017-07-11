#! /usr/bin/python

import sys
import math

cur_context = ""
cur_count = {}
context = ""
count = {}
sum_count = 0
prob = []
H_prob = 0
for line in sys.stdin:
	line = line.strip()
	context, count = line.split('\t',1)
	count = eval(count)	
	
	if context == cur_context:
		cur_count.update(count)
	else:
		for item in cur_count:
			sum_count += int(cur_count[item])

		for item in cur_count:
			temp = float(cur_count[item])/float(sum_count)
			H_prob -=  temp*math.log(temp,2)
		
		if cur_context :
			print("{0}\t{1}".format(cur_context,H_prob))

		sum_count = 0
		H_prob = 0
		cur_context = context
		cur_count = count

if context == cur_context:
	for item in cur_count:
        	sum_count += int(cur_count[item])
	for item in cur_count:
        	temp = float(cur_count[item])/float(sum_count)
                H_prob -=  temp*math.log(temp,2)
        if cur_context :
                print("{0}\t{1}".format(cur_context,H_prob))

