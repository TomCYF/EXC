#! /usr/bin/python
import sys

count = 0
for line in sys.stdin:
	if count < 10:
		print line.strip()
		count += 1
