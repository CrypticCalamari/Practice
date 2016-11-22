#!/usr/bin/python3.5

import random, sys, time

def ngram_count(text):
	out = dict()
	for i in range(1,len(text)):
		for j in range(len(text)-i):
			count = 0
			ngram = text[j:j+i]
			if ngram not in out:
				for k in range(j, len(text)-i):
					if ngram == text[k:k+i]:
						count += 1
				out[ngram] = count
	return out

text = sys.argv[1]

print(text)
out = ngram_count(text)

for k in sorted(out.keys()):
	print(k, ":", out[k])

