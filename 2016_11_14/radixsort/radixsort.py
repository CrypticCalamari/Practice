#!/usr/bin/python3

import random, sys, time

def radixsort(a):
	more = 1
	mask = 1
	level = 0
	out = a[:]
	bins = [[], []]
	while more:
		more = 0
		for x in out:
			shift = x >> level
			bins[shift & mask].append(x)
			more |= shift
		out = bins[0] + bins[1]
		bins = [[], []]
		level += 1
	return out

def validate(a):
	if len(a) <= 1:
		return True
	for i in range(1, len(a)):
		if a[i] < a[i-1]:
			return False
	return True

size = int(sys.argv[1])
test = []
for i in range(size):
	test.append(random.randrange(100000))

print("===============================================================================")
print(test)
out = radixsort(test)
print(out)
print("Is Valid:", validate(out))
print("===============================================================================")

