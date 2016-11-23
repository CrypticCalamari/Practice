#!/usr/bin/python3.5

import sys

def unigram_count(t):
	out = dict()
	for i in t:
		if i in out:
			out[i] += 1
		else:
			out[i] = 1
	return out

t = sys.argv[1]
out = unigram_count(t)
for i in sorted(out.keys()):
	print(i, ":", out[i])


