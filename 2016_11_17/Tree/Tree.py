#!/usr/bin/python3.5

import random, sys

class Tree:
	def __init__(self):
		self.data = None
		self.left = None
		self.right = None
	def insert(self, data):
		if not self.data:
			self.data = data
			self.left = Tree()
			self.right = Tree()
			return
		tail = self.left if data <= self.data else self.right
		tail.insert(data)
	@staticmethod
	def inorder(node, op):
		if node.data:
			Tree.inorder(node.left, op)
			op(node.data)
			Tree.inorder(node.right, op)
	def contains(self, data):
		if self.data:
			if data < self.data:
				tail = self.left
			elif data > self.data:
				tail = self.right
			else:
				return True
		else:
			return False
		return tail.contains(data)

size = int(sys.argv[1])
test = Tree()
t = []
out = []
for i in range(size):
	r = random.randrange(size)
	test.insert(r)
	t.append(r)

print(t)
Tree.inorder(test, out.append)
print(out)

for i in range(size):
	print(i, ": ", test.contains(i))





