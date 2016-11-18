#!/usr/bin/python3.5

import random, sys, time

# LSD Radix Sort
def radixsort(a):
	level = 0
	more = 1
	temp = a[:]
	bins = [[], []]
	while more:
		more = 0
		for i in temp:
			shifted = i >> level
			bins[shifted % 2].append(i)
			more |= shifted
		temp = bins[0] + bins[1]
		bins = [[], []]
		level += 1
	return temp

def validate(a):
	for i in range(1, len(a)):
		if a[i] < a[i-1]:
			return False
	return True

size = int(sys.argv[1])
test = [] #list(range(size))
#random.shuffle(test)
for i in range(size):
	test.append(random.randrange(size))

print("===============================================================================")
if size < 32: print(test)
begin = time.time()
out = radixsort(test)
end = time.time()
if size < 32: print(out)
print("Is Valid:", validate(out))
print("Elapsed:", int(round((end - begin) * 1)), "s")
print("Elapsed:", int(round((end - begin) * 1000)), "ms")
print("Elapsed:", int(round((end - begin) * 1000000)), "micro s")
print("Elapsed:", int(round((end - begin) * 1000000000)), "ns")
print("===============================================================================")







