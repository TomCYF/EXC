#! /usr/bin/python

import sys

pre_word = ""
pre_file = ""
data = {}
file_count = 0
count = 0
for line in sys.stdin:
	items = line.strip().split()
	
	if pre_word == items[0]:
		if pre_file == items[1]:
			count += int(items[2])
		else:
			file_count += 1
			pre_file = items[1]
			data[items[1]] = count
	else:
		if pre_word:
			print_str = ""
			it = 0
			temp_data = sorted(data)
	       		for item in temp_data:
				if it != len(data)-1:
		       			print_str += ("(" + item + "," + str(data[item]) + "), ")
					it += 1
				else:
					print_str += ("(" + item + "," + str(data[item]) + ")")
	       		print("{0} : {1} : {{{2}}}".format(pre_word,file_count,print_str))

		pre_word = items[0]
		pre_file = items[1]
		count = int(items[2])
		file_count = 1
		data = {}
		data[items[1]] = int(items[2])

if pre_word:
	print_str = ""
	it = 0
	temp_data = sorted(data)
	for item in temp_data:
		if it != len(data)-1:
               		print_str += ("(" + item + "," + str(data[item]) + "), ")
			it += 1
		else:
			print_str += ("(" + item + "," + str(data[item]) + ")") 





