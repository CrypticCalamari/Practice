#!/usr/bin/python3

import random, sys, time

# Failed to recall this one. Kept thinking of shell sort.
def comb(a):
	swap = True
	g = len(a)
	while g > 1 or swap:
		swap = False
		g = max(1, int(g/1.3))
		for i in range(g, len(a)):
			if a[i] < a[i-g]:
				a[i], a[i-g] = a[i-g], a[i]
				swap = True

size = int(sys.argv[1])
test = list(range(size))

print("===============================================================================")
print("Random distinct")
random.shuffle(test)
if size < 32: print(test)
begin = time.time()
comb(test)
end = time.time()
if size < 32: print(test)
print("Time:", int(round((end - begin))), "s")
print("Time:", int(round((end - begin) * 1000)), "ms")
print("Time:", int(round((end - begin) * 1000000)), "μs")
print("Time:", int(round((end - begin) * 1000000000)), "ns")
print("===============================================================================")

print("===============================================================================")
print("Reverse distinct")
test.reverse()
if size < 32: print(test)
begin = time.time()
comb(test)
end = time.time()
if size < 32: print(test)
print("Time:", int(round((end - begin))), "s")
print("Time:", int(round((end - begin) * 1000)), "ms")
print("Time:", int(round((end - begin) * 1000000)), "μs")
print("Time:", int(round((end - begin) * 1000000000)), "ns")
print("===============================================================================")

print("===============================================================================")
print("Random non-distinct")
test = []
for i in range(size):
	test.append(random.randrange(size))
if size < 32: print(test)
begin = time.time()
comb(test)
end = time.time()
if size < 32: print(test)
print("Time:", int(round((end - begin))), "s")
print("Time:", int(round((end - begin) * 1000)), "ms")
print("Time:", int(round((end - begin) * 1000000)), "μs")
print("Time:", int(round((end - begin) * 1000000000)), "ns")
print("===============================================================================")

print("===============================================================================")
print("Reverse non-distinct")
test.reverse()
if size < 32: print(test)
begin = time.time()
comb(test)
end = time.time()
if size < 32: print(test)
print("Time:", int(round((end - begin))), "s")
print("Time:", int(round((end - begin) * 1000)), "ms")
print("Time:", int(round((end - begin) * 1000000)), "μs")
print("Time:", int(round((end - begin) * 1000000000)), "ns")
print("===============================================================================")








