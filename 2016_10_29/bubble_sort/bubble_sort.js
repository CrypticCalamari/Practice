#!/usr/bin/node

function bubble_sort(a) {
	for (let x in a)
		for (let y = 1; y <= a.length - x; y++)
			if (a[y] < a[y-1])
				[a[y], a[y-1]] = [a[y-1], a[y]];
}





// Test
let test = [];
for (let i = 0; i < 20; i++)
	test.push(i);

for (let i = 0; i < 20; i++) {
	let n = Math.floor(Math.random() * (20 - i) + i);
	[test[i], test[n]] = [test[n], test[i]];
}
console.log(test);
bubble_sort(test);
console.log(test);

