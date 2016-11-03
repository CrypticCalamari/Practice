#!/usr/bin/python3

import random;
import sys;
import time;

def mergesort(a):
	if len(a) <= 1:
		return a
	mid = len(a) // 2
	left = mergesort(a[:mid])
	right = mergesort(a[mid:])
	if left[mid-1] < right[0]:
		return left + right
	return merge(left, right)

def merge(left, right):
	m = list()
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			m.append(left[i])
			i += 1
		else:
			m.append(right[j])
			j += 1
	m += left[i:]
	m += right[j:]
	return m

size = int(sys.argv[1])
test = list(range(size))
random.shuffle(test)
#print(test)

if len(test) < 32: print(test)
begin = time.time()
merged = mergesort(test)
end = time.time()
if len(test) < 32: print(merged)

print("Nano Elapsed: ", int(round((end - begin) * 1000000)))








