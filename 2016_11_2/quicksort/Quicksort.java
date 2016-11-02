import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

class Quicksort {
	public static void main(String... args) {
		int size = Integer.parseInt(args[0]);
		int[] test = new int[size];
		for (int i = 0; i < size; i++)
			test[i] = i;
		for (int i = 0; i < size; i++) {
			int r = ThreadLocalRandom.current().nextInt(i, size);
			int t = test[i];
			test[i] = test[r];
			test[r] = t;
		}

		System.out.println(Arrays.toString(test));
		sort(test);
		System.out.println(Arrays.toString(test));
	}
	public static void sort(int[] a) {
		quicksort(a, 0, a.length - 1);
	}
	public static void quicksort(int[] a, int lo, int hi) {
		if (lo < hi) {
			int p = partition(a, lo, hi);
			quicksort(a, lo, p-1);
			quicksort(a, p+1, hi);
		}
	}
	public static int partition(int[] a, int lo, int hi) {
		int p = a[lo];
		int i = lo;
		int j = hi;
		while (true) {
			while (a[i] < p)
				i++;
			while (a[j] > p)
				j--;
			if (i >= j)
				return j;
			int t = a[i];
			a[i] = a[j];
			a[j] = t;
		}
	}
}







