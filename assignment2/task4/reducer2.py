#! /usr/bin/python

import sys

pre_PId = ""
pre_OUId = ""
count = 0
ans_list = []
max_count = 0
max_list = []
max_OUId = ""


for line in sys.stdin:
	OUId, PId, val = line.strip().split()
	if OUId == pre_OUId:
		count += 1
		ans_list.append(PId)
	else:
		if count > max_count:
			max_count = count
			max_list = ans_list
			max_OUId = pre_OUId
		pre_OUId = OUId
		count = 1
		ans_list = []
		ans_list.append(PId)

if count > max_count:
	max_count = count
	max_list = ans_list
	max_OUId = pre_OUId

temp_str = ""
for i in range(len(max_list)):
	if i == len(max_list)-1:
		temp_str += max_list[i]
	else:
		temp_str += max_list[i] + ", "

print("{0} -> {1}, {2}".format(max_OUId,max_count,temp_str)) 
		
