#!/usr/bin/node

function insertion(a) {
	for (let i = 1; i < a.length; i++) {
		let t = a[i];
		let k = i;
		while (k > 0 && t < a[k-1]) {
			a[k] = a[k-1];
			k--;
		}
		a[k] = t;
	}
}

let size = parseInt(process.argv[2]);
let test = [];
for (let i = 0; i < size; i++)
	test.push(i);
for (let i = 0; i < size; i++) {
	let r = Math.floor(Math.random() * (size - i)) + i;
	[test[i],test[r]] = [test[r],test[i]];
}
console.log(test);
insertion(test);
console.log(test);











