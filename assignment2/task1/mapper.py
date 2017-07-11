#! /usr/bin/python

import sys
import os

for line in sys.stdin:
	words = line.strip().split()
	for word in words:
		file_path = os.environ["mapreduce_map_input_file"]
		file = file_path.split('/')[-1]
        	print("{0}\t{1}\t{2}".format(word,file,1))
 

