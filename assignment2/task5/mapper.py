#! /usr/bin/python

import sys
import random

resevoir_count = 0
sample_line = ""
for line in sys.stdin:
	if random.randint(0, resevoir_count) == 0:
		sample_line = line.strip()
	resevoir_count += 1

print("{0}\t{1}".format(sample_line,resevoir_count))
