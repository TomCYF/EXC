#! /usr/bin/python

import sys

pre_word = ""
pre_file = ""
count = 0
for line in sys.stdin:
	items = line.strip().split()
	
	if pre_word == items[0] and pre_file == items[1]:
		count += 1
	else:
		if pre_word:
			print ("{0}\t{1}\t{2}".format(pre_word, pre_file, count))
		pre_word = items[0]
		pre_file = items[1]
		count = 1
if pre_word:
	print ("{0}\t{1}\t{2}".format(pre_word, pre_file, count))
