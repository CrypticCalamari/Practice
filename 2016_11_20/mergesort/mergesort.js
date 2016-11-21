#!/usr/bin/nodejs
"use strict";

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
	while (i < left.length) {
		m.push(left[i]);
		i++;
	}
	while (j < right.length) {
		m.push(right[j]);
		j++;
	}
	return m;
}

function mergesort(a) {
	if (a.length <= 1)
		return a;
	let mid = Math.floor(a.length / 2);
	let left = mergesort(a.slice(0, mid));
	let right = mergesort(a.slice(mid));
	return merge(left, right);
}

let size = parseInt(process.argv[2]);
let test = [];
for (let i = 0; i < size; i++)
	test.push(i);
for (let i = 0; i < size; i++) {
// Working on a new box and didn't realize I had an older version of nodejs installed. TIL to be careful about begign ES6 features.
	let r = Math.floor(Math.random() * (size - i)) + i;
	let t = test[i];
	test[i] = test[r]
	test[r] = t;
}

console.log(test);
let out = mergesort(test);
console.log(out);








