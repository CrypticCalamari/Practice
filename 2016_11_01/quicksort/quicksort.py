#!/usr/bin/python3

import random
import sys

def partition(a, lo, hi):
	p = a[lo]
	i = lo
	j = hi
	while True:
		while a[i] < p:
			i += 1
		while a[j] > p:
			j -= 1
		if i >= j:
			return j
		a[i],a[j] = a[j],a[i]

def quicksort(a, lo, hi):
	if lo < hi:
		p = partition(a, lo, hi)
		quicksort(a, lo, p-1)
		quicksort(a, p+1, hi)

size = int(sys.argv[1])
test = list(range(size))
random.shuffle(test)
print(test)
quicksort(test, 0, size-1)
print(test)

