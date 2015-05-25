import java.util.ArrayList;
import java.util.Arrays;


public class Euler62 {


	Euler62() {
		ArrayList<int[]> tenDigits = new ArrayList<int[]>();
		ArrayList<int[]> elevenDigits = new ArrayList<int[]>();
		for (long i = 1000; i < 2155; i++) {
			tenDigits.add(JMath.permutate(i*i*i));
		}
		for (long i = 2156; i < 9999; i++) {
			elevenDigits.add(JMath.permutate(i*i*i));
		}
		//check ten digits
		int count = 0;
		for (int[] digits : tenDigits) {
			count = 0;
			for (int[] otherDigits : tenDigits) {
				if (Arrays.equals(digits, otherDigits)) {
					count++;
				}
			}
			System.out.println(count);
			System.out.println(tenDigits.indexOf(digits)+1000);
			if(count == 5) {

				break;
			}
		}
		//check eleven digits

		for (int[] digits : elevenDigits) {
			count = 0;
			for (int[] otherDigits : elevenDigits) {
				if (Arrays.equals(digits, otherDigits)) {
					count++;
				}
			}
			System.out.println(count);
			System.out.println(elevenDigits.indexOf(digits)+2156);
			if(count == 5) {

				break;
			}
		}
	}


}
