#! /usr/bin/python

import sys
from heapq import heappush, heapreplace

data_list = ['Id','PostTypeId','ViewCount','OwnerUserId','AcceptedAnswerId','LastEditorUserId',
'AnswerCount','CommentCount','Score']
parse_data = {}
pq = []

for line in sys.stdin:
	words = line.strip().split()
	for item in words:
		for key in data_list:
			key_str = key + '=\"'
			if item.startswith(key_str):
				parse_data[key] = item[item.find("\"")+1:-1]
				break;	
	if parse_data['PostTypeId'] == '1':
		#print("{0} {1}".format(parse_data['ViewCount'],parse_data['Id']))
		if len(pq) < 10:
			heappush(pq,(int(parse_data['ViewCount']),parse_data['Id']))
		elif parse_data['ViewCount'] > pq[0][0]:
			heapreplace(pq,(int(parse_data['ViewCount']),parse_data['Id']))
			
	parse_data = {}

for i in range(len(pq)):
	print ("{0} {1}".format(pq[i][0],pq[i][1]))
