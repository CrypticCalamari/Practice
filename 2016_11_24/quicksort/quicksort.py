#!/usr/bin/python3

import random, sys, time

def pivot(a, lo, hi):
	# Median of Three
	b = random.randrange(lo, hi+1)
	c = random.randrange(lo, hi+1)
	d = random.randrange(lo, hi+1)
	if a[b] < a[c]:
		if a[c] < a[d]:
			return c
		else:
			if a[b] < a[d]:
				return d
			else:
				return b
	else:
		if a[b] < a[d]:
			return b
		else:
			if a[c] < a[d]:
				return d
			else:
				return c

def partition(a, lo, hi):
	x = pivot(a, lo, hi)
	a[x], a[lo] = a[lo], a[x]
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
test = []
for i in range(size):
	test.append(random.randrange(size))

print("===============================================================================")
if size < 32: print(test)
begin = time.time()
quicksort(test, 0, size-1)
end = time.time()
if size < 32: print(test)
print("Is Valid:", validate(test))
print("===============================================================================")
print("Elapsed:", int(round((end - begin) * 1)), "s")
print("Elapsed:", int(round((end - begin) * 1000)), "ms")
print("Elapsed:", int(round((end - begin) * 1000000)), "ms")
print("Elapsed:", int(round((end - begin) * 1000000000)), "ns")
print("===============================================================================")
test = []
for i in range(size):
	test.append(i)
print("===============================================================================")
if size < 32: print(test)
begin = time.time()
quicksort(test, 0, size-1)
end = time.time()
if size < 32: print(test)
print("Is Valid:", validate(test))
print("===============================================================================")
print("Elapsed:", int(round((end - begin) * 1)), "s")
print("Elapsed:", int(round((end - begin) * 1000)), "ms")
print("Elapsed:", int(round((end - begin) * 1000000)), "ms")
print("Elapsed:", int(round((end - begin) * 1000000000)), "ns")
print("===============================================================================")
test = []
for i in range(size):
	test.append(size-i)
print("===============================================================================")
if size < 32: print(test)
begin = time.time()
quicksort(test, 0, size-1)
end = time.time()
if size < 32: print(test)
print("Is Valid:", validate(test))
print("===============================================================================")
print("Elapsed:", int(round((end - begin) * 1)), "s")
print("Elapsed:", int(round((end - begin) * 1000)), "ms")
print("Elapsed:", int(round((end - begin) * 1000000)), "ms")
print("Elapsed:", int(round((end - begin) * 1000000000)), "ns")
print("===============================================================================")









