#!/usr/bin/node

function merge(left, right) {
	let i = 0;
	let j = 0;
	let m = [];
	while (i < left.length && j < right.length) {
		if (left[i] <= right[j]) {
			m.push(left[i]);
			i++;
		} else {
			m.push(right[j]);
			j++;
		}
	}
	m.push(...left.slice(i));
	m.push(...right.slice(j));
	return m;
}
function mergesort(a) {
	if (a.length <= 1)
		return a;
	let mid = Math.floor(a.length / 2);
	let left = mergesort(a.slice(0,mid));
	let right = mergesort(a.slice(mid));
	if (left[mid-1] <= right[0]) {
		left.push(...right);
		return left;
	}
	return merge(left, right);
}

let size = parseInt(process.argv[2]);
let test = [];
for (let i = 0; i < size; i++)
	test.push(i);
for (let i = 0; i < size; i++) {
	let r = Math.floor(Math.random() * (size - i)) + i;
	[test[i], test[r]] = [test[r], test[i]];
}

console.log(test);
let out = mergesort(test);
console.log(out);






