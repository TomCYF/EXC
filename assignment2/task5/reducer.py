#!/usr/bin/python

import sys
import random

number = 0
num_list = []
line_list = []
for line in sys.stdin:
	line = line.strip()
	word, num = line.split('\t')
	number += int(num)
	num_list.append(num)
	line_list.append(word)

ran = random.randint(0,number)
pre = 0
for it in range(len(num_list)):
	if ran >= pre and ran < num_list[it]:
		print line_list[it]
		break
	pre = num_list[it] 
