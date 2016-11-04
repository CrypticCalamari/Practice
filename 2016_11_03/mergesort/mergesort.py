#!/usr/bin/python3

import random, sys, time

def merge(left, right):
	x = 0
	y = 0
	m = []
	while x < len(left) and y < len(right):
		if left[x] < right[y]:
			m.append(left[x])
			x += 1
		else:
			m.append(right[y])
			y += 1
	m += left[x:]
	m += right[y:]
	return m

def mergesort(a):
	if len(a) <= 1:
		return a
	mid = len(a) // 2
	left = mergesort(a[:mid])
	right = mergesort(a[mid:])
	if left[mid-1] <= right[0]:
		return left + right
	return merge(left, right)

size = int(sys.argv[1])
test = [] #list(range(size))
#random.shuffle(test)
for i in range(size):
	test.append(random.randrange(size))

print("--------------------------------------------------------------------------------")
if size < 30: print(test)

begin = time.time()
merged = mergesort(test)
end = time.time()

if size < 30: print(merged)
print("Time:", int(round(end - begin)), "s")
print("Time:", int(round((end - begin) * 1000)), "ms")
print("Time:", int(round((end - begin) * 1000000)), "μs")
print("Time:", int(round((end - begin) * 1000000000)), "ns")
print("--------------------------------------------------------------------------------")


















