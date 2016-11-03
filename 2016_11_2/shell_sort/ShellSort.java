import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

class ShellSort {
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
		shell(test);
		System.out.println(Arrays.toString(test));
	}
	public static void shell(int[] a) {
		int g = a.length / 2;
		while (g > 0) {
			for (int i = g; i < a.length; i++) {
				int t = a[i];
				int j;
				for (j = i; j >= g; j -= g) {
					if (t < a[j-g])
						a[j] = a[j-g];
					else
						break;
				}
				a[j] = t;
			}
			g /= 2;
		}
	}
}
