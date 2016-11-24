#!/usr/bin/python3.5

import math, random, sys, Heap

def count(t):
	d = dict()
	for x in t:
		if x in d:
			d[x] += 1
		else:
			d[x] = 1
	return d

def in_order(code, prefix, d):
	if type(code[1]) == type(str()):
		d[code[1]] = prefix
		return

	in_order(code[1][0], prefix + b'0', d)
	in_order(code[1][1], prefix + b'1', d)

def huffman_coding(d):
	h = Heap.Heap()
	for x in d:
		h.put(d[x], x)

	while h.size() > 1:
		a = h.get()
		b = h.get()
		c = a[0] + b[0]
		h.put(c, (a, b))

	return h.get()


t = sys.argv[1]
d = count(t)
for i in sorted(d.keys()):
	print("key:", i, ", item:", d[i])

code = huffman_coding(d)
print(code)
d = dict()
prefix = bytes()
in_order(code, prefix, d)

for i in sorted(d.keys()):
	print(i, ":", d[i])

encoded_t = bytes()
for x in t:
	encoded_t += d[x]

print(encoded_t)
print(len(encoded_t))

bt = []
x = 0
for i in range(len(encoded_t)):
	if not i % 8:
		bt.append(x)
		x = 0
	if encoded_t[i] == 49:
		x |= 1
		x <<= 1
if len(encoded_t) % 8:
	bt.append(x)

j = 0
while True:
	x = 0
	for i in range(8):
		if encoded_t[j] == 49:
			x |= 1
			x <<= 1
		j += 1
		if j == len(encoded_t):
			break
	if j == len(encoded_t):

		break
	bt.append(x)
bt.append(

print(bt)

f = open("test.out", 'wb')
for i in bt:
	print(i)
	f.write(i.to_bytes(1, byteorder='big'))
f.close()

# Took me a while, but I finally managed to figure out binary data manipulation in python to a certain extent.

f = open("test.out", 'rb')
stuff = f.read()
print(stuff)






