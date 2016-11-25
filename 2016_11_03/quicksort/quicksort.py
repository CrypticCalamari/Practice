#!/usr/bin/python3

import random, sys, time

# TIL: Be wary of Wikipedia and vary your test data.
# -----------------------------------------------------------------------------
# The partition algorithm below came from wikipedia. I fixed it up a bit
# because the one on Wikipedia had pointless increments that caused index out
# of range errors, and so it appeared to work fine after that, but that was
# only on data with distinct values. When you introduce non-distinct values, it
# hangs on the if statement, because i and j never meet.

# Addendum: In looking for a correct version of this algorithm, it appears that
# there are many incorrect versions of this algorithm; almost suspiciously
# many. It's as if people who post this algorithm online intentionally post the
# incorrect / incomplete version.

# Incorrect version
def semi_correct_partition(a, lo, hi):
	p = a[lo]
	i = lo
	j = hi
	while True:
		while a[i] < p:
			i += 1
		while a[j] > p:
			j -= 1
		if i >= j:
			return j
		a[i], a[j] = a[j], a[i]

# Correct version
def partition(a, lo, hi):
	p = a[lo]
	i = lo
	j = hi
	while i < j:
		while i < len(a) and a[i] <= p:
			i += 1
		while a[j] > p:
			j -= 1
		if i < j:
			a[i], a[j] = a[j], a[i]
	a[lo] = a[j]
	a[j] = p
	return j

def quicksort(a, lo, hi):
	if lo < hi:
		p = partition(a, lo, hi)
		quicksort(a, lo, p-1)
		quicksort(a, p+1, hi)

size = int(sys.argv[1])
test = []

print("--------------------------------------------------------------------------------")
for i in range(size):
	test.append(random.randrange(size))
print("Random Test")
if size < 32: print(test)
begin = time.time()
quicksort(test, 0, len(test)-1)
end = time.time()
if size < 32: print(test)
print("Time:", int(round(end - begin)), "s")
print("Time:", int(round((end - begin) * 1000)), "ms")
print("Time:", int(round((end - begin) * 1000000)), "ms")
print("Time:", int(round((end - begin) * 1000000000)), "ns")
print("--------------------------------------------------------------------------------")

print("--------------------------------------------------------------------------------")
test = list(range(size))
random.shuffle(test)
print("Distinct Shuffle Test")
if size < 32: print(test)
begin = time.time()
quicksort(test, 0, len(test)-1)
end = time.time()
if size < 32: print(test)
print("Time:", int(round(end - begin)), "s")
print("Time:", int(round((end - begin) * 1000)), "ms")
print("Time:", int(round((end - begin) * 1000000)), "ms")
print("Time:", int(round((end - begin) * 1000000000)), "ns")
print("--------------------------------------------------------------------------------")

test.reverse()
print("--------------------------------------------------------------------------------")
print("Distinct Reverse Test")
if size < 32: print(test)
begin = time.time()
quicksort(test, 0, len(test)-1)
end = time.time()
if size < 32: print(test)
print("Time:", int(round(end - begin)), "s")
print("Time:", int(round((end - begin) * 1000)), "ms")
print("Time:", int(round((end - begin) * 1000000)), "ms")
print("Time:", int(round((end - begin) * 1000000000)), "ns")
print("--------------------------------------------------------------------------------")





