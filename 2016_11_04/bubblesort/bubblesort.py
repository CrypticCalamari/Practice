#!/usr/bin/python3

import random, sys, time

def bubble(a):
	for i in range(len(a)):
		swap = False
		for j in range(1, len(a)-i):
			if a[j] < a[j-1]:
				a[j], a[j-1] = a[j-1], a[j]
				swap = True
		if not swap:
			break

size = int(sys.argv[1])
test = list(range(size))
random.shuffle(test)
#for i in range(size):
	#test.append(random.randrange(size))
print("===============================================================================")
if size < 32: print(test)
begin = time.time()
bubble(test)
end = time.time()
if size < 32: print(test)
print("Time:", int(round((end - begin))), "s")
print("Time:", int(round((end - begin) * 1000)), "ms")
print("Time:", int(round((end - begin) * 1000000)), "μs")
print("Time:", int(round((end - begin) * 1000000000)), "ns")
print("===============================================================================")










