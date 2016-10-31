#!/usr/bin/node

function comb(a) {
	let gap = a.length;
	let swaps = true;
	while (gap > 1 || swaps) {
		gap = Math.max(1, Math.floor(gap / 1.3));
		swaps = false;
		for (let i = 0; i < a.length - gap; i++) {
			let j = i + gap;
			if (a[i] > a[j]) {
				swaps = true;
				[a[i], a[j]] = [a[j], a[i]];
			}
		}
	}
}
let size = Number.parseInt(process.argv[2]);
let test = [];
for (let i = 0; i < size; i++)
	test.push(i);

for (let i = 0; i < size; i++) {
	let j = Math.floor(Math.random() * (size - i)) + i;
	[test[i], test[j]] = [test[j], test[i]];
}

console.log(test);
comb(test);
console.log(test);
