#!/usr/bin/python3

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class List:
	def __init__(self):
		self.size = 0
		self.begin = None
	
	def append(self, data):
		n = Node(data)
		if not self.begin:
			self.begin = n
			return
		c = self.begin
		while c.next:
			c = c.next
		c.next = n
		self.size += 1

	def insert(self, i, data):
		n = Node(data)
		if not self.begin:
			self.begin = n
			return
		if i < 0:
			raise IndexError("Out of range / not implemented for negative values.")
		if i == 0:
			n.next = self.begin
			self.begin = n
			return
		c = self.begin
		j = 1
		while j < i and c.next:
			c = c.next
			j += 1
		n.next = c.next
		c.next = n
		self.size += 1

	def iterate(self):
		c = self.begin
		while c:
			yield c.data
			c = c.next

	def pop(self, i=self.size-1):
		if not self.begin:
			raise IndexError("Can't pop; empty")
		j = 0






test = List()
for i in range(5):
	test.append(i)



for i in test.iterate():
	print(i)















