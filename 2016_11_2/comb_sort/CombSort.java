import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

class CombSort {
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
		comb(test);
		System.out.println(Arrays.toString(test));
	}
	public static void comb(int[] a) {
		boolean swap = true;
		int g = a.length;
		while (g > 1 || swap) {
			swap = false;
			g = Math.max(1, (int)(g/1.3));
			for (int i = 0; i < a.length - g; i++) {
				if (a[i] > a[i+g]) {
					int t = a[i];
					a[i] = a[i+g];
					a[i+g] = t;
					swap = true;
				}
			}
		}
	}
}
