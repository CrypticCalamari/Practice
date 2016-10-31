#!/usr/bin/node

function bubble_sort(a) {
	for (i in a)
		for (let j = 1; j <= a.length - i; j++)
			if (a[j] < a[j - 1])
				[a[j], a[j - 1]] = [a[j - 1], a[j]];
}

let a = [];



























