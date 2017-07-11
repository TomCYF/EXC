#!/usr/bin/python

import sys
from struct import unpack, pack, calcsize

count = 1
size = 1000
e = 0.01
fre_dic = {}
stream_count = {}
cur_stream = 1

for line in sys.stdin:
	line = line.strip()
	count += 1
	if line not in fre_dic:
		stream_count[line] = cur_stream - 1
		fre_dic[line] = 1
	else:
		fre_dic[line] += 1
	if count % size == 0:
		for item, num in fre_dic.items():
			if num <= cur_stream - stream_count[item]:
				del fre_dic[item]
				del stream_count[item]
		cur_stream += 1

for item, num in fre_dic.items():
	if num > e * count - 0.1 * e * count:
		print ("{0}".format(item))
		 
