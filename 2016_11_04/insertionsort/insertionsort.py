#!/usr/bin/python3

import random, sys, time

def insertion(a):
	for i in range(1, len(a)):
		m = a[i]
		k = i
		for j in range(i, 0, -1):
			if m < a[j-1]:
				a[j] = a[j-1]
				k -= 1
		a[k] = m

size = int(sys.argv[1])
test = list(range(size))
random.shuffle(test)
print("===============================================================================")
if size < 32: print(test)
begin = time.time()
insertion(test)
end = time.time()
if size < 32: print(test)
print("Time:", int(round((end - begin))), "s")
print("Time:", int(round((end - begin) * 1000)), "ms")
print("Time:", int(round((end - begin) * 1000000)), "μs")
print("Time:", int(round((end - begin) * 1000000000)), "ns")
print("===============================================================================")

