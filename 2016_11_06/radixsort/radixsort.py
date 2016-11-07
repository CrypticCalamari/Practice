#!/usr/bin/python3

import random, sys, time

# Only works with values >= 0
def radix(a):
	more = 1
	level = 0
	mask = 1
	out = a[:]
	buckets = [[], []]
	while more:
		more = 0
		for i in out:
			shifted = i >> level
			buckets[shifted & mask].append(i)
			more |= shifted
		out = buckets[0] + buckets[1]
		buckets = [[], []]
		level += 1
	return out

def verify(a):
	for i in range(1, len(a)):
		if a[i] < a[i-1]:
			return False
	return True

size = int(sys.argv[1])
test = list(range(size))

print("===============================================================================")
print("Shuffled sort")
random.shuffle(test)

if size < 32: print(test)
begin = time.time()
out = radix(test)
correct = verify(out)
end = time.time()
if size < 32: print(out)

print("Correct:", correct)
print("Time:", int(round((end - begin))), "s")
print("Time:", int(round((end - begin) * 1000)), "ms")
print("Time:", int(round((end - begin) * 1000000)), "μs")
print("Time:", int(round((end - begin) * 1000000000)), "ns")
print("===============================================================================")

print("===============================================================================")
print("Random sort")
test = []
for i in range(size):
	test.append(random.randrange(size))

if size < 32: print(test)
begin = time.time()
out = radix(test)
correct = verify(out)
end = time.time()
if size < 32: print(out)

print("Correct:", correct)
print("Time:", int(round((end - begin))), "s")
print("Time:", int(round((end - begin) * 1000)), "ms")
print("Time:", int(round((end - begin) * 1000000)), "μs")
print("Time:", int(round((end - begin) * 1000000000)), "ns")
print("===============================================================================")

print("===============================================================================")
print("Collated sort")
test = []
for i in range(size):
	test.append(i % 2)

if size < 32: print(test)
begin = time.time()
out = radix(test)
correct = verify(out)
end = time.time()
if size < 32: print(out)

print("Correct:", correct)
print("Time:", int(round((end - begin))), "s")
print("Time:", int(round((end - begin) * 1000)), "ms")
print("Time:", int(round((end - begin) * 1000000)), "μs")
print("Time:", int(round((end - begin) * 1000000000)), "ns")
print("===============================================================================")











