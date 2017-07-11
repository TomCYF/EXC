#!/usr/bin/python

import sys
import math
import hashlib
from struct import unpack, pack, calcsize

if len(sys.argv)==2:
	num_key = sys.argv[1]
else: 
	num_key = 1897987
num_bits = num_key * 7

bitarray = []

hashfn = hashlib.md5
num_hashes = 7

#Initialise hash function
salts = tuple(hashfn(hashfn(pack('I', i)).digest()) for i in range(num_hashes))


#Initialise the bitarray
for i in range(num_bits):
	bitarray.append(False)

#Bloom Filter
for line in sys.stdin:
	line = line.strip()
	key = line.encode('utf-8')
	pos = []
	for salt in salts:
        	h = salt.copy()
        	h.update(key)
		count = 0	
		for item in unpack('Q'*2,h.digest()):
			pos.append(item%num_bits)
	contain = True
	for it in pos:
		if not bitarray[it]:
			contain = False
		
	if not contain:
		print line
		for it in pos:
			bitarray[it] = True
			#print ("Set{0} True".format(it))
	pos = []

#print bitarray
			
	

	
