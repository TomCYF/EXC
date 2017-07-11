#! /usr/bin/python

import sys

tag = ""
stuid = '-1'
stuname = ""

grades = {}

max_average = 0
max_name = []

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
			temp_sum = 0
			temp_count = 0
			temp_ave = 0
			for item in grades:
				temp_sum += int(grades[item])
				temp_count += 1
			if temp_count > 3:
				temp_ave = float(temp_sum/temp_count)
			if temp_ave > max_average:
				max_average = temp_ave
				max_name = []
				max_name.append(stuname)
			#if temp_ave == max_average:
			#	max_name.append(stuname)

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

temp_sum = 0
temp_count = 0
temp_ave = 0
for item in grades:
	temp_sum += int(grades[item])
	temp_count += 1
if temp_count > 3:
	temp_ave = float(temp_sum/temp_count)
if temp_ave > max_average:
	max_average = temp_ave
	max_name = []
	max_name.append(stuname)
#if temp_ave == max_average:
#	max_name.append(stuname)

for i in max_name:
	print("{0}".format(i))




