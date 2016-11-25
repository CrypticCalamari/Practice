import Heap
class Huffman:
	def __init__(self, text):
		if type(text) is not type(str()):
			raise TypeError("text parameter should be a string")
		self.text = text
		self.code_tree = None
		self.code_table = None
		self.pre_encoding = None
		self.encoding = None
		self.frequency = None
	def get_frequency(self):
		if self.frequency:
			return self.frequency

		self.frequency = dict()
		for x in self.text:
			if x in self.frequency:
				self.frequency[x] += 1
			else:
				self.frequency[x] = 1
		return self.frequency

	def get_code_tree(self):
		if self.code_tree:
			return self.code_tree
		
		if len(self.frequency) == 0:
			self.get_frequency()

		heap = Heap.Heap()
		for x in sorted(self.frequency.keys()):
			heap.put(self.frequency[x], x)

		while heap.size() > 1:
			a = heap.get()			# new left branch
			b = heap.get()			# new right branch
			c = a[0] + b[0]			# Add frequencies of each new branch
			heap.put(c, [a, b])

		self.code_tree = heap.get()
		return self.code_tree

	def get_code_table(self):
		if self.code_table:
			return self.code_table

		if not self.code_tree:
			self.get_code_tree()

		self.code_table = dict()
		prefix = b''
		self.get_code_table_helper(self.code_tree, prefix, self.code_table)
		return self.code_table

	def get_code_table_helper(self, tree, prefix, table):
		if type(tree[1]) == type(str()):
			table[tree[1]] = prefix
			return

		self.get_code_table_helper(tree[1][0], prefix + b'0', table)
		self.get_code_table_helper(tree[1][1], prefix + b'1', table)

	def get_pre_encoding(self):
		if self.pre_encoding:
			return self.pre_encoding

		if not self.code_table:
			self.get_code_table()

		self.pre_encoding = b''
		for x in self.text:
			self.pre_encoding += self.code_table[x]

		return self.pre_encoding

	def get_encoding(self):
		if self.encoding:
			return self.encoding

		if not self.pre_encoding:
			self.get_pre_encoding()

		self.encoding = []

		j = 0
		while True:
			byte = 0
			for i in range(8):
				byte <<= 1
				if self.pre_encoding[j] == 49:	# 49 == '1'
					byte |= 1
				j += 1
				if j == len(self.pre_encoding):
					break
			self.encoding.append(byte)
			if j == len(self.pre_encoding):
				break

		return self.encoding

	def save_to_file(self, file_name):
		if not self.encoding:
			self.get_encoding()

		with open(file_name, 'wb') as f:
			for b in self.encoding:
				f.write(b.to_bytes(1, byteorder='little'))

h = Huffman("This is a test")
print(h.text)
print(h.get_frequency())
print(h.get_code_tree())
t = h.get_code_table()
for k in sorted(t.keys()):
	print(k, ":", t[k])

print(h.get_pre_encoding())
print(h.get_encoding())

h.save_to_file("TEST.out")

r = ''
with open('TEST.out', 'rb') as f:
	r = f.read(1)
	while r:
		print(int.from_bytes(r, byteorder='little'))
		r = f.read(1)





