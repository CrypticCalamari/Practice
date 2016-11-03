#!/usr/bin/python3

import random

# Stupid gnome
def gnome(a):
	i = 1
	while i < len(a):
		if i == 0 or a[i] >= a[i-1]:
			i += 1
		else:
			a[i],a[i-1] = a[i-1],a[i]
			i -= 1

# Teleporting gnome
def gnome2(a):
	i = 1
	j = 2 # teleport index
	while i < len(a):
		if a[i-1] <= a[i]:
			i = j
			j += 1
		else:
			a[i],a[i-1] = a[i-1],a[i]
			i -= 1
			if i == 0:
				i = j
				j += 1


test = list(range(20))
random.shuffle(test)
print("Stupid gnome and his inability to teleport:")
print(test)
gnome(test)
print(test)

random.shuffle(test)
print("Smarter gnome paid attention during lessons in teleportation:")
print(test)
gnome2(test)
print(test)
