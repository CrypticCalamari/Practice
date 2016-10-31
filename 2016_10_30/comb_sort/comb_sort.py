#!/usr/bin/python3

import random
import sys

def comb(a):
	c = 0
	gap = len(a)
	swaps = True
	while gap > 1 or swaps:
		gap = max(1, int(gap / 1.3))
		swaps = False
		for i in range(len(a) - gap):
			c += 1
			j = i + gap
			if a[i] > a[j]:
				a[i], a[j] = a[j], a[i]
				swaps = True
	print("Comparisons: ", c)

size = int(sys.argv[1])
test = list(range(size))
random.shuffle(test)

if size <= 33: print(test)
comb(test)
if size <= 33: print(test)
