#!/usr/bin/python3

import random
import sys

def bubble(a):
	c = 0
	for i in range(len(a)):
		swaps = 0
		for j in range(1,len(a)-i):
			c += 1
			if a[j] < a[j-1]:
				swaps += 1
				a[j], a[j-1] = a[j-1], a[j]
		if swaps == 0:
			break
	print("comparisons: ", c)

size = int(sys.argv[1])
test = list(range(size))
random.shuffle(test)

if size <= 33: print(test)
bubble(test)
if size <= 33: print(test)
