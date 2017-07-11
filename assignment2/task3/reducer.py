#! /usr/bin/python

import sys

pre_OUId = ""
pre_PId = []
count = 0
max_OUId = ""
max_PId = []
max_count = 0
for line in sys.stdin:
	OUId, ParId, PId = line.strip().split()
	
	if OUId == pre_OUId:
		if ParId not in pre_PId:
			pre_PId.append(ParId)
			count += 1
	else:
		if pre_OUId and count > max_count:
			max_OUId = pre_OUId
			max_PId = pre_PId
			max_count = count
		pre_OUId = OUId
		count = 1
		pre_PId = []
		pre_PId.append(ParId)

if pre_OUId and count > max_count:
	max_OUId = pre_OUId
        max_PId = pre_PId
        max_count = count

temp_str = ""
for i in range(max_count):
	if i != (max_count-1):
		temp_str += max_PId[i] + ', '
	else:
		temp_str += max_PId[i]
print("{0} -> {1}".format(max_OUId,temp_str))
