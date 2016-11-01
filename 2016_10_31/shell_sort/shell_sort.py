#!/usr/bin/python3

import random

# More swaps than necessary, but more elegant and easier to understand
# Extraneous swaps can easily be removed, when optimization is required
# The examples of this online show premature optimization in my opinion
# which obfuscates the structure of the algorithm. It's kind of funny
# that most versions use the version with fewer swaps while also using
# the version with the simplest gap sequence, which also results in the
# worst case time complexity of θ(N^2) when N = 2^p.

# One of the obfuscations that is particularly annoying is putting an
# unnecessary conjunction in the loop case,

def shell(a):
	g = len(a) // 2
	while g > 0:
		for i in range(g, len(a)):
			for j in range(i, 0, -g):
				if a[j] < a[j-g]:
					a[j], a[j-g] = a[j-g], a[j]
				else:
					break
		g //= 2

test = list(range(20))
random.shuffle(test)
print(test)
shell(test)
print(test)

