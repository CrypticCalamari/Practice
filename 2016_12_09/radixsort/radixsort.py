#!/usr/bin/python3

import random, sys, time

def radixsort(a):
	out = a[:]
	bins = [[], []]
	mask = 1
	more = 1
	level = 0
	while more:
		more = 0
		for x in out:
			shifted = x >> level
			bins[mask & shifted].append(x)
			more |= shifted
		out = bins[0] + bins[1]
		bins = [[], []]
		level += 1
	return out

size = int(sys.argv[1])
test = []
for i in range(size):
	test.append(random.randrange(size))

print(test)
out = radixsort(test)
print(out)
