import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

class BubbleSort {
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
		bubble(test);
		System.out.println(Arrays.toString(test));
	}
	public static void bubble(int[] a) {
		for (int i = 0; i < a.length; i++) {
			for (int j = 1; j < a.length - i; j++) {
				if (a[j] < a[j-1]) {
					int t = a[j];
					a[j] = a[j-1];
					a[j-1] = t;
				}
			}
		}
	}
}
