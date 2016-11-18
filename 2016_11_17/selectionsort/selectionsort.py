#!/usr/bin/python3.5

import random, sys, time

def selection(a):
	for i in range(len(a)):
		m = a[i]
		k = i
		for j in range(i, len(a)):
			if a[j] < m:
				m = a[j]
				k = j
		a[k] = a[i]
		a[i] = m

size = int(sys.argv[1])
test = []
for i in range(size):
	test.append(random.randrange(size))

print(test)
selection(test)
print(test)










