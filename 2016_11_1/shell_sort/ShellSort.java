import java.util.ArrayList;
import java.util.Collections;
import java.util.concurrent.ThreadLocalRandom; // Unused due to using Collections.shuffle instead of custom shuffle

class ShellSort {
	public static void main(String... args) {
		int size = Integer.parseInt(args[0]);
		ArrayList<Integer> test = new ArrayList<Integer>();
		for (int i = 0; i < size; i++)
			test.add(i);
		Collections.shuffle(test);
		System.out.println(test.toString());
		shell(test);
		System.out.println(test.toString());
	}

	// Using ArrayList to practice the Java standard library and nothing more.
	public static <T extends Comparable<? super T>> void shell(ArrayList<T> a) {
		int g = a.size() / 2;
		while (g > 0) {
			for (int i = g; i < a.size(); i++) {
				for (int j = i; j - g >= 0; j -= g) {
					if (a.get(j).compareTo(a.get(j-g)) < 0) {
						T t = a.get(j);
						a.set(j, a.get(j-g));
						a.set(j-g, t);
					}
					else
						break;
				}
			}
			g /= 2;
		}
	}
}
