#!/usr/bin/python3

import random;
import sys;

def sort(a):
	quicksort(a, 0, len(a)-1)

def partition(a, lo, hi):
	p = a[lo]
	x = lo
	y = hi
	while True:
		while a[x] < p:
			x += 1
		while a[y] > p:
			y -= 1
		if x >= y:
			return y
		a[x],a[y] = a[y],a[x]

def quicksort(a, lo, hi):
	if lo < hi:
		p = partition(a, lo, hi)
		quicksort(a, lo, p-1)
		quicksort(a, p+1, hi)

size = int(sys.argv[1])
test = list(range(size))
random.shuffle(test)
print(test)
sort(test)
print(test)
