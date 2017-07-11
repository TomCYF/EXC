#! /usr/bin/python

import sys

total_num = 0
prev_seq = ""
seq = ""

for line in sys.stdin:
	line = line.strip()
	seq, num = line.split("\t",1)
	num = int(num)

	if prev_seq == seq:
		total_num += num
	else:
		if prev_seq:
			print("{0}\t{1}".format(prev_seq, total_num))

		total_num = num
		prev_seq = seq

if prev_seq == seq:
	print("{0}\t{1}".format(prev_seq, total_num))
