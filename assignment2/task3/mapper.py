#! /usr/bin/python

import sys
data_list = ['Id','PostTypeId','ViewCount','OwnerUserId','AcceptedAnswerId','LastEditorUserId',
'AnswerCount','CommentCount','Score','ParentId']
parse_data = {}


for line in sys.stdin:
	words = line.strip().split()
	for item in words:
		for key in data_list:
			key_str = key + '=\"'
			if item.startswith(key_str):
				parse_data[key] = item[item.find("\"")+1:-1]
				break;	
	if parse_data['PostTypeId'] == '2':
		print("{0} {1} {2}".format(parse_data['OwnerUserId'],parse_data['ParentId'],parse_data['Id']))
	parse_data = {}

