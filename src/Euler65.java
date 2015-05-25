import java.math.BigInteger;
import java.util.Arrays;


public class Euler65 {
	public Euler65() {
		System.out.println(JMath.digitAdd(nthCovergent(100, 1)[0].toString()));
	}
	
	/**
	 * gets the fraction representation of the continued fraction for e
	 * if you go n terms deep
	 * @param n
	 * @return numerator in [0], denominator in [1]
	 */
	private BigInteger[] nthCovergent (int n, int currentTerm) {
		if (currentTerm == n){
			if (currentTerm == 1) {
				BigInteger num = new BigInteger("2");
				BigInteger denom = new BigInteger("1");
				return new BigInteger[] {num, denom};
				
			}
			else if (currentTerm % 3 == 0) {
				BigInteger a = new BigInteger(Integer.toString(2 * (currentTerm / 3)));
				BigInteger num = a;
				BigInteger denom = new BigInteger("1");
				return new BigInteger[] {num, denom};
			}
			else if (currentTerm % 3 != 0) {
				BigInteger a = new BigInteger("1");
				BigInteger num = a;
				BigInteger denom = new BigInteger("1");
				return new BigInteger[] {num, denom};
			}
		}
		else if (currentTerm == 1) {
			BigInteger[] lastFrac = nthCovergent(n, currentTerm+1);
			BigInteger num = ((lastFrac[0].multiply(new BigInteger("2"))).add(lastFrac[1]));
			BigInteger denom = lastFrac[0];
			return new BigInteger[] {num, denom};
			
		}
		else if (currentTerm % 3 == 0) {
			BigInteger a = new BigInteger(Integer.toString(2 * (currentTerm / 3)));
			BigInteger[] lastFrac = nthCovergent(n, currentTerm+1);
			BigInteger num = (lastFrac[0].multiply(a)).add(lastFrac[1]);
			BigInteger denom = lastFrac[0];
			return new BigInteger[] {num, denom};
		}
		else if (currentTerm % 3 != 0) {
			BigInteger a = new BigInteger("1");
			BigInteger[] lastFrac = nthCovergent(n, currentTerm+1);
			BigInteger num = (lastFrac[0].multiply(a)).add(lastFrac[1]);
			BigInteger denom = lastFrac[0];
			return new BigInteger[] {num, denom};
		}

		return new BigInteger[] {new BigInteger("1"), new BigInteger("1")};
			
	}
}
