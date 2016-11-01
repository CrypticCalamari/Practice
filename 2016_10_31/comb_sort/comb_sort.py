#!/usr/bin/python3

import random

def comb(a):
	gap = len(a)
	swaps = True
	while gap > 1 or swaps:
		gap = max(1, int(gap / 1.3))
		swaps = False
		for i in range(len(a) - gap):
			j = i + gap
			if a[i] > a[j]:
				swaps = True
				a[i], a[j] = a[j], a[i]

test = list(range(20))
random.shuffle(test)
print(test)
comb(test)
print(test)
