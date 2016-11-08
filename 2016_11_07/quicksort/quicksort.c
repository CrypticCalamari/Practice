#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int partition(int a[], int len, int lo, int hi) {
	int p = a[lo];
	int i = lo;
	int j = hi;
	while (i < j) {
		while (i < len && a[i] <= p) {
			i++;
		}
		while (a[j] > p) {
			j--;
		}
		if (i < j) {
			int t = a[i];
			a[i] = a[j];
			a[j] = t;
		}
	}
	a[lo] = a[j];
	a[j] = p;
	return j;
}
void quicksort(int a[], int len, int lo, int hi) {
	if (lo < hi) {
		int p = partition(a, len, lo, hi);
		quicksort(a, len, lo, p-1);
		quicksort(a, len, p+1, hi);
	}
}

int main(int argc, char* argv[]) {
	int size; sscanf(argv[1], "%d", &size);
	int test[size];
	for (int i = 0; i < size; i++) {
		test[i] = i;
	}
	srand(time(NULL));
	for (int i = 0; i < size; i++) {
		int r = rand() % (size - i) + i;
		int t = test[i];
		test[i] = test[r];
		test[r] = t;
	}

	if (size < 32) {
		printf("[");
		for (int i = 0; i < size-1; i++) {
			printf("%d, ", test[i]);
		}
		printf("%d]\n", test[size-1]);
	}

	clock_t begin = clock();
	quicksort(test, size, 0, size-1);
	clock_t end = clock();

	if (size < 32) {
		printf("[");
		for (int i = 0; i < size-1; i++) {
			printf("%d, ", test[i]);
		}
		printf("%d]\n", test[size-1]);
	}

	clock_t elapsed = end - begin;

	printf("Begin: %d µs\n", begin);
	printf("End: %d µs\n", end);
	printf("Time: %d µs\n", elapsed);
}
















