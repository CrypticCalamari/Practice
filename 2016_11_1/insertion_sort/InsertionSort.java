import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

class InsertionSort {
	public static void main(String... args) {
		int size = Integer.parseInt(args[0]);
		int[] a = new int[size];
		for (int i = 0; i < size; i++)
			a[i] = i;
		shuffle(a);
		System.out.println(Arrays.toString(a));
		insertion(a);
		System.out.println(Arrays.toString(a));
	}
	public static void insertion(int[] a) {
		for (int i = 1; i < a.length; i++) {
			int t = a[i];
			int k = i;
			while (k > 0 && t < a[k-1]) {
				a[k] = a[k-1];
				k--;
			}
			a[k] = t;
		}
	}
	public static void shuffle(int[] a) {
		for (int i = 0; i < a.length; i++) {
			int r = ThreadLocalRandom.current().nextInt(i, a.length);
			int t = a[i];
			a[i] = a[r];
			a[r] = t;
		}
	}
}
