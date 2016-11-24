#!/usr/bin/python3

# count frequencies
# create huffman tree
# turn tree into prefix table

# use prefix table together with text input to create binary pre-output

# or

# use prefix table with text input to create and write binary output in one step
# to account for potentially limited memory if input text is too large.

# If the former then convert the "binary" to bytes integer types 8 bits at a
# time and then write those numbers to file using to_bytes(1, byteorder='little')

def frequency_count(t):
	o = dict()
	for c in t:
		if c in o:
			o[c] += 1
		else:
			o[c] = 1
	return o

def encode(i, r, o):
	if not len(i):
		return

	rbl = r.bit_length()
	n = i.pop()
	nbl = n.bit_length()

	t = 0
	if rbl + nbl <= 8:
		t = r << nbl
		t = r | n
		r = 0
	else:
		t = r << (8 - rbl)
		t = r | (n >> (rbl + nbl - 8))
		# Finish calculating new r








