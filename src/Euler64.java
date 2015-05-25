import java.util.List;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;


public class Euler64 {
	
	Euler64() {
		JMath.startTimer();
		int odds = 0;
		for (int x = 1; x <= 10000; x++) {
			if ((Math.sqrt(x) != Math.floor(Math.sqrt(x)) && findPeriod(x) % 2 != 0)) {
				odds++;
			}
		}
		System.out.println(odds);
		JMath.endTimer();

	}

	/**
	 * gets the period of the continued fraction of that number
	 * algorithm from http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method
	 * @param number
	 * @return
	 */
	private int findPeriod(int number) {
		double m = 0;
		double d = 1;
		int a0 = (int) Math.floor(Math.sqrt(number));
		int a = a0;
		
		int period = 0;
		
		while (a != 2*a0) {
			m = (d*a) - m;
			d = (number - (m*m))/d;
			a = (int) Math.floor((a0 + m)/d);
			period++;
		}
		return period;
	}
	

	
}
	
