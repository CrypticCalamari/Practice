#!/usr/bin/node

function partition(a, lo, hi) {
	let p = a[lo];
	let i = lo;
	let j = hi;
	while (true) {
		while (a[i] < p)
			i++;
		while (a[j] > p)
			j--;
		if (i >= j)
			return j;
		[a[i], a[j]] = [a[j], a[i]];
	}
}

function quicksort(a, lo, hi) {
	if (lo < hi) {
		let p = partition(a, lo, hi);
		quicksort(a, lo, p-1);
		quicksort(a, p+1, hi);
	}
}

let size = parseInt(process.argv[2]);
let test = [];
for (let i = 0; i < size; i++)
	test.push(i);
for (let i = 0; i < size; i++) {
	let r = Math.floor(Math.random() * (test.length - i)) + i;
	[test[i], test[r]] = [test[r], test[i]];
}

console.log(test);
quicksort(test, 0, size-1);
console.log(test);









