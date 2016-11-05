#!/usr/bin/python3

import random, sys, time

def selection(a):
	for i in range(len(a)-1):
		m = a[i]
		k = i
		for j in range(i+1, len(a)):
			if a[j] < m:
				m = a[j]
				k = j
		a[i], a[k] = a[k], a[i]

size = int(sys.argv[1])
test = list(range(size))
random.shuffle(test)
print("===============================================================================")
if size < 32: print(test)
begin = time.time()
selection(test)
end = time.time()
if size < 32: print(test)
print("Time:", int(round((end - begin))), "s")
print("Time:", int(round((end - begin) * 1000)), "ms")
print("Time:", int(round((end - begin) * 1000000)), "μs")
print("Time:", int(round((end - begin) * 1000000000)), "ns")
print("===============================================================================")






