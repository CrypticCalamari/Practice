#!/usr/bin/python3

import random, sys, time

def shell(a):
	g = len(a) // 2
	while g > 0:
		for i in range(g, len(a)):
			for j in range(i,0, -g):
				if a[j] < a[j-g]:
					a[j], a[j-g] = a[j-g], a[j]
				else:
					break
		g //= 2

def shell2(a):
	g = len(a) // 2
	while g > 0:
		for i in range(g, len(a)):
			t = a[i]
			k = i
			for j in range(i,0, -g):
				if t < a[j-g]:
					a[j] = a[j-g]
					k -= g
				else:
					break
			a[k] = t
		g //= 2

size = int(sys.argv[1])
test = list(range(size))

print("===============================================================================")
print("Random distinct")
random.shuffle(test)
if size < 32: print(test)
begin = time.time()
shell2(test)
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
shell2(test)
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
shell2(test)
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
shell2(test)
end = time.time()
if size < 32: print(test)
print("Time:", int(round((end - begin))), "s")
print("Time:", int(round((end - begin) * 1000)), "ms")
print("Time:", int(round((end - begin) * 1000000)), "μs")
print("Time:", int(round((end - begin) * 1000000000)), "ns")
print("===============================================================================")








