#!/usr/bin/python3

import random, sys, time

def comb(a, shrink):
	g = len(a)
	swap = True
	while g > 1 or swap:
		g = max(1, int(g/shrink))
		swap = False
		for i in range(g, len(a)):
			if a[i] < a[i-g]:
				a[i], a[i-g] = a[i-g], a[i]
				swap = True

size = int(sys.argv[1])
test = [] #list(range(size))
#random.shuffle(test)
for i in range(size):
	test.append(random.randrange(size))

print(test)
begin = time.time()
comb(test, 1.3)
end = time.time()
print(test)
