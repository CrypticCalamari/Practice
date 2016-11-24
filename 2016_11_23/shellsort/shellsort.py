#!/usr/bin/python3.5

import random, sys, time

def shell(a):
	g = len(a) // 2
	while g > 0:
		for i in range(g, len(a)):
			for j in range(i, 0, -g):
				if a[j] < a[j-g]:
					a[j], a[j-g] = a[j-g], a[j]
		g //= 2

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
print(test)
shell(test)
print(test)
print("===============================================================================")
print("Is Valid:", validate(test))
print("===============================================================================")
