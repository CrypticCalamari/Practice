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
		
	}
}
