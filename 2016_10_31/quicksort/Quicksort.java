import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

public class Quicksort {
	public static void main(String... args) {
		int size = Integer.parseInt(args[0]);
		int[] test = new int[size];
		for (int i = 0; i < size; i++)
			test[i] = i;
		for (int i = 0; i < size; i++) {
			int r = ThreadLocalRandom.current().nextInt(i,size);
			int t = test[i];
			test[i] = test[r];
			test[r] = t;
		}

		System.out.println(Arrays.toString(test));
		quicksort(test, 0, size - 1);
		System.out.println(Arrays.toString(test));
	}

	public static int partition(int[] a, int lo, int hi) {
		int p = a[lo];
		while (true) {
			while (a[lo] < p)
				lo++;
			while (a[hi] > p)
				hi--;
			if (lo >= hi)
				return hi;
			int t = a[lo];
			a[lo] = a[hi];
			a[hi] = t;
		}
	}

	public static void quicksort(int[] a, int lo, int hi) {
		if (lo < hi) {
			int p = partition(a, lo, hi);
			quicksort(a, lo, p-1);
			quicksort(a, p+1, hi);
		}
	}
}
