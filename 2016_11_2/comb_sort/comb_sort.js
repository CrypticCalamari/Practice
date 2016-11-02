#!/usr/bin/node

function comb(a) {
	let swap = true;
	let g = a.length;
	while (g > 1 || swap) {
		g = Math.floor(g/1.3);
		swap = false;
		for (let i = 0; i < a.length - g; i++) {
			if (a[i] > a[i+g]) {
				[a[i],a[i+g]] = [a[i+g],a[i]];
				swap = true;
			}
		}
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
comb(test);
console.log(test);















