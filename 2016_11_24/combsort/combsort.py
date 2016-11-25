#!/usr/bin/python3

import random, sys, time

def comb(a):
	swap = True
	g = len(a)
	while g > 1 or swap:
		g = max(1, int(g / 1.3))
		swap = False
		for i in range(g, len(a)):
			if a[i] < a[i-g]:
				a[i], a[i-g] = a[i-g], a[i]
				swap = True

def validate(a):
	for i in range(1, len(a)):
		if a[i] < a[i-1]:
			return False
	return True

size = int(sys.argv[1])
test = []
for i in range(size):
	test.append(random.randrange(size))

print(test)
comb(test)
print(test)
print("Is Valid:", validate(test))
