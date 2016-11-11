#!/usr/bin/python3

import random, sys, time

def partition(a, lo, hi):
	p = a[lo]
	i = lo
	j = hi
	while i < j:
		while i < len(a) and a[i] <= p:
			i += 1
		while a[j] > p:
			j -= 1
		if i < j:
			a[i], a[j] = a[j], a[i]
	a[lo], a[j] = a[j], a[lo]
	return j

def quicksort(a, lo, hi):
	if lo < hi:
		p = partition(a, lo, hi)
		quicksort(a, lo, p-1)
		quicksort(a, p+1, hi)

def validate(a):
	for i in range(1, len(a)):
		if a[i] < a[i-1]:
			return False
	return True

size = int(sys.argv[1])
test = list(range(size))
random.shuffle(test)

print(test)
quicksort(test, 0, size-1)
print(test)
print("Is Valid:", validate(test))
















