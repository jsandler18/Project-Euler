import java.math.BigInteger;


public class Euler66 {
	public Euler66() {
		JMath.startTimer();
		BigInteger largest = new BigInteger("0");
		double largestD = 0;
		for (int i = 2; i <= 1000; i++) {
			if (!JMath.isPerfectSquare(i)) {
				System.out.println(i);
				BigInteger tmp = getMinX(i);
				if (tmp.compareTo(largest) > 0) {
					largest = tmp;
					largestD = i;
				}
			}
		}
		System.out.println(largest + ", " + largestD);
		JMath.endTimer();
	}
	
	/**
	 * returns first integer solution of x = sqrt (1+d*y*y)
	 * @param d
	 * @return
	 */
	private BigInteger getMinX(int d) {
		int i = 2;
		BigInteger[] frac = JMath.nthContinuedFraction(d, i);
		BigInteger x = frac[0].pow(2).subtract(new BigInteger(Integer.toString(d)).multiply(frac[1].pow(2)));
		while (!x.equals(new BigInteger("1"))) {
			frac = JMath.nthContinuedFraction(d, ++i);
			x = frac[0].pow(2).subtract(new BigInteger(Integer.toString(d)).multiply(frac[1].pow(2)));
		}
		return frac[0];
	}
}
