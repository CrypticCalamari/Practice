#!/usr/bin/python3.5

import random, sys, time

def radix(a):
	level = 0
	more = 1
	out = a[:]
	bins = [[], []]
	while more:
		more = 0
		for i in out:
			shifted = i >> level
			bins[shifted % 2].append(i)
			more |= shifted
		level += 1
		out = bins[0] + bins[1]
		bins = [[], []]
	return out

def validate(a):
	for i in range(1, len(a)):
		if a[i] < a[i-1]:
			a[i], a[i-1] = a[i-1], a[i]
	return True

size = int(sys.argv[1])
t = []
for i in range(size):
	t.append(random.randrange(size))

print("===============================================================================")
print(t)
out = radix(t)
print(out)
print("Is Valid:", validate(out))
print("===============================================================================")







