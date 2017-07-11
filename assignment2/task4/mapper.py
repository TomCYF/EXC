#! /usr/bin/python

import sys
data_list = ['Id','PostTypeId','ViewCount','OwnerUserId','AcceptedAnswerId','LastEditorUserId',
'AnswerCount','CommentCount','Score']
parse_data = {}


for line in sys.stdin:
	words = line.strip().split()
	for item in words:
		for key in data_list:
			key_str = key + '=\"'
			if item.startswith(key_str):
				parse_data[key] = item[item.find("\"")+1:-1]
				break;
	if parse_data.has_key('AcceptedAnswerId') and parse_data['PostTypeId'] == '1':
		print("{0}".format(parse_data['AcceptedAnswerId']))		
	else:
		print("{0} {1}".format(parse_data['Id'],parse_data['OwnerUserId']))
	parse_data = {}

