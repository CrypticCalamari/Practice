#!/usr/bin/python3

import random, sys, time, copy

# In my opinion, this implementation looks clearer, but I saw that I'm creating
# a 2 new ranges each time through the outer loop, so I decided to test and
# compare this with the Rosetta code implementation. Looks like my version is
# ever so slightly faster.
def cocktail(a):
	for i in range(len(a)//2):
		swap = False
		for j in range(1+i, len(a)-i):
			if a[j] < a[j-1]:
				a[j], a[j-1] = a[j-1], a[j]
				swap = True
		if not swap:
			break
		swap = False
		for j in range(len(a)-i-1, i, -1):
			if a[j] < a[j-1]:
				a[j], a[j-1] = a[j-1], a[j]
				swap = True
		if not swap:
			break

# Rosetta Code implementation below for comparison
# Inspection this further it seems this implementation is slower due to the
# reversed() function. Tested this via the timeit module below.
def cocktailSort(A):
	up = range(len(A)-1)
	while True:
		for indices in (up, reversed(up)):
			swapped = False
			for i in indices:
				if A[i] > A[i+1]:  
					A[i], A[i+1] =  A[i+1], A[i]
					swapped = True
			if not swapped:
				return


size = int(sys.argv[1])
test = list(range(size))
random.shuffle(test)
other = test[:]
#test.reverse()
#for i in range(size):
	#test.append(random.randrange(size))

print("===============================================================================")
print("My implementation")
if size < 32: print(test)
begin = time.time()
cocktail(test)
end = time.time()
if size < 32: print(test)
print("Time:", int(round((end - begin))), "s")
print("Time:", int(round((end - begin) * 1000)), "ms")
print("Time:", int(round((end - begin) * 1000000)), "μs")
print("Time:", int(round((end - begin) * 1000000000)), "ns")
print("===============================================================================")


print("===============================================================================")
print("RosettaCode.org implementation")
if size < 32: print(other)
begin = time.time()
cocktailSort(other)
end = time.time()
if size < 32: print(other)
print("Time:", int(round((end - begin))), "s")
print("Time:", int(round((end - begin) * 1000)), "ms")
print("Time:", int(round((end - begin) * 1000000)), "μs")
print("Time:", int(round((end - begin) * 1000000000)), "ns")
print("===============================================================================")

import timeit

print("print(timeit.timeit('for i in range(10): pass', setup=''))")
print(timeit.timeit("for i in range(10): pass", setup=""))
print("print(timeit.timeit('for i in reversed(range(10)): pass', setup=''))")
print(timeit.timeit("for i in reversed(range(10)): pass", setup=""))


