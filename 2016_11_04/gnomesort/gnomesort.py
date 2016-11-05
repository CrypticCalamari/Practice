#!/usr/bin/python3

import random, sys, time

# Failed to recall this one.

def gnome(a):
	i = 1
	while i < len(a):
		if i == 0 or a[i] >= a[i-1]:
			i += 1
		else:
			a[i], a[i-1] = a[i-1], a[i]
			i -= 1

def gnome2(a):
	i = 1
	j = 2
	while i < len(a):
		if a[i] > a[i-1]:
			i = j
			j += 1
		else:
			a[i], a[i-1] = a[i-1], a[i]
			i -= 1
			if i == 0:
				i = j
				j += 1

size = int(sys.argv[1])
test = list(range(size))
random.shuffle(test)

print("===============================================================================")
print("gnome")
if size < 32: print(test)
begin = time.time()
gnome(test)
end = time.time()
if size < 32: print(test)
print("Time:", int(round((end - begin))), "s")
print("Time:", int(round((end - begin) * 1000)), "ms")
print("Time:", int(round((end - begin) * 1000000)), "μs")
print("Time:", int(round((end - begin) * 1000000000)), "ns")
print("===============================================================================")

random.shuffle(test)
print("===============================================================================")
print("gnome 2 (teleporting)")
if size < 32: print(test)
begin = time.time()
gnome2(test)
end = time.time()
if size < 32: print(test)
print("Time:", int(round((end - begin))), "s")
print("Time:", int(round((end - begin) * 1000)), "ms")
print("Time:", int(round((end - begin) * 1000000)), "μs")
print("Time:", int(round((end - begin) * 1000000000)), "ns")
print("===============================================================================")






