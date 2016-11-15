#!/usr/bin/python3.4

import os, psutil, random, sys, time

class Node:
	def __init__(self, data=None):
		self.next = None
		self.data = data

class List:
	def __init__(self):
		self.head = None
		self.tail = None

	def push_front(self, data):
		n = Node(data)
		n.next = self.head
		self.head = n
		if not self.tail:
			self.tail = self.head
	def push_back(self, data):
		n = Node(data)
		if not self.head:
			self.head = n
			self.tail = n
			return
		self.tail.next = n
		self.tail = n
	def pop_front(self):
		if not self.head:
			return None
		t = self.head
		self.head = self.head.next
		if self.tail is t:
			self.tail = None
		return t.data
	def pop_back(self):
		if not self.head:
			return None
		c = self.head
		while c is not self.tail:
			c = c.next
		t = c.data
		c.next = None
		self.tail = c
		return t
	def empty(self):
		return not self.head
	def size(self):
		i = 0
		n = self.head
		while n:
			i += 1
			n = n.next
		return i
	def iterate(self):
		c = self.head
		while c:
			yield c.data
			c = c.next

test = List()
#for i in range(1000000):
	#test.push_back(i)
"""
process = psutil.Process(os.getpid())
print(process.memory_info().rss)
test.head = None
test.tail = None
print(process.memory_info().rss)
"""
for i in range(10):
	test.push_back(random.randrange(100))

for i in test.iterate():
	sys.stdout.write(str(i))
	sys.stdout.write(" ")
sys.stdout.write("\n")
sys.stdout.flush()

end = input("Press ENTER to end ...")



















