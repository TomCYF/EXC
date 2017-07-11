#! /usr/bin/python

import sys
import random

num = 100
samples = []
count = 0

for line in sys.stdin:
	if count < num:
		samples.append(line.strip())
	else:
		r = random.randint(0,count-1)
		if r < num:
			samples[r] = line.strip()
	count += 1

for item in samples:
	print item
