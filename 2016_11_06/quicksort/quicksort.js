#!/usr/bin/node

function partition(a, lo, hi) {
	let p = a[lo];
	let i = lo;
	let j = hi;
	while (i < j) {
		while (i < a.length && a[i] <= p)
			i++;
		while (a[j] > p)
			j--;
		if (i < j)
			[a[i], a[j]] = [a[j], a[i]];
	}
	[a[lo], a[j]] = [a[j], a[lo]];
	return j
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
/*for (let i = 0; i < size; i++)
	test.push(i);
for (let i = 0; i < size; i++) {
	let r = Math.floor(Math.random() * (size - i)) + i;
	[test[i], test[r]] = [test[r], test[i]];
}*/
for (let i = 0; i < size; i++)
	test.push(Math.floor(Math.random() * size));
console.log(test);
quicksort(test, 0, size-1);
console.log(test);
