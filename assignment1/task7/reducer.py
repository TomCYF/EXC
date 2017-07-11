#! /usr/bin/python

import sys

tag = ""
stuid = '-1'
stuname = ""

grades = {}

for line in sys.stdin:
	
	line = line.strip()
	tokens = line.split()

	tag = tokens[1]
	if stuid == tokens[0]:
		if tag == 'mark':
			grades[tokens[2]] = tokens[3]
		else:
			stuname = tokens[2]	
	else:
		if stuname:
			temp_str = ""
			for item in grades:
				temp_str += ("("+item+" "+grades[item]+")  ")
			print("{0} --> {1}".format(stuname,temp_str))
			
			if tag == 'mark':
				stuid = tokens[0]
				stuname = ""
				grades = {}
				grades[tokens[2]] = tokens[3]
			else:
				stuid = tokens[0]
				stuname = tokens[2]
				grades = {}
		else:
			if tag == 'mark':
				stuid = tokens[0]
				grades[tokens[2]] = tokens[3]
			else:
				stuid = tokens[0]
				stuname = tokens[2]

temp_str = ""
for item in grades:
	temp_str += ("("+item+" "+grades[item]+")  ")
print("{0} --> {1}".format(stuname,temp_str))




