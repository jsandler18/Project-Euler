
import java.util.List;
import java.math.BigInteger;
import java.time.Instant;
import java.util.ArrayList;

/**
 * a class full of miscellaneous and half-useful methods
 * @author Jake
 *
 */
public class JMath{
	//Program timing
	private static long startTime;
	private static long endTime;
	private static int startTimeNano;
	private static int endTimeNano;
	
	/**
	 * Will start a timer for the program.  Will overwrite any previous timers currently running.
	 */
	public static void startTimer(){
		Instant start = Instant.now();
		startTime=start.getEpochSecond();
		startTimeNano=start.getNano();
	}
	
	/**
	 * Will end a started timer and print the results.  Will cause a runtime error if startTimer() isn't called first.
	 */
	public static void endTimer(){
		Instant end = Instant.now();
		endTime=end.getEpochSecond();
		endTimeNano=end.getNano();
		System.out.println((endTime-startTime)+"."+(endTimeNano-startTimeNano) + "s");
	}

	//obscure math functions
	
	/**
	 * returns the nth continued fraction of the square root of the given number
	 * throws illegal argument exception if the given  number is a perfect square
	 * @param number
	 * @param n
	 * @return
	 */
	public static BigInteger[] nthContinuedFraction(int number, int n) { 
		if (JMath.isPerfectSquare(number)) {
			throw new IllegalArgumentException("No perfect Squares");
		}
		else {
			//find constants
			List<Long> constants= new ArrayList<Long>();
			double m = 0;
			double d = 1;
			long a0 = (long) Math.floor(Math.sqrt(number));
			long a = a0;
			long period = 0;
			
			while (a != 2*a0) {
				m = (d*a) - m;
				d = (number - (m*m))/d;
				a = (long) Math.floor((a0 + m)/d);
				period++;
				constants.add(a);
			}
			n -= 2;
			BigInteger lastNum = new BigInteger(Long.toString(constants.get((n%constants.size()))));
			BigInteger lastDenom = new BigInteger("1");
			BigInteger num = new BigInteger("0");
			BigInteger denom = new BigInteger("0");
			for (int i = n-1 ; i >=0; i--) {
				num = new BigInteger(Long.toString(constants.get(i%constants.size())));
				num = (num.multiply(lastNum)).add(lastDenom);
				denom = lastNum;
				lastNum = num;
				lastDenom = denom;
			}
			num = new BigInteger(Long.toString(a0));
			num = (num.multiply(lastNum)).add(lastDenom);
			denom = lastNum;
			lastNum = num;
			lastDenom = denom;
			return new BigInteger[] {lastNum, lastDenom};
		}
	}
	
	/**
	 * tests if the the number is 1-n pandigital, where n is the largest digit in the number
	 * @param 
	 * @return boolean value
	 */
	public static boolean isPandigital(int test){
		int[] digit = digitSplit(test);
		int size=0;
		for(int i = 0; i <digit.length; i++){
			if(digit[i]>size){
				size=digit[i];
			}
		}
		if(digit.length==size){
			for(int a = 0; a<digit.length; a++){
				if(digit[a]==0){
					return false;
				}
				for(int b = a+1; b<digit.length; b++){
					if(digit[a]==digit[b]){
						return false;
					}
				}
			}
			return true;
		}
		return false;
	}
	
	/**
	 * Tests if the given String is the same both backwards and forwards.
	 * Works on numbers, words and phrases.
	 * @param testString
	 * @return boolean value
	 */
	public static boolean isPalindrome(String test){
		char[] chars = test.toCharArray();
		for(int x = 0; x<(chars.length/2)+1;x++){
			if(chars[x]!=chars[chars.length-1-x]){
				return false;
			}
		}
		return true;
	}

	
	//number manipulation
	
	/**
	 * takes the given number and returns an array that has the counts
	 * of the number of digits in the number.  The idex corresponds
	 * to the digit, and the data at that index is the number of occurences of that digit
	 * @param num
	 * @return
	 */
	public static int[] permutate(long num) {
		int[] digits = digitSplit(num);
		int[] counts = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		for (int i = 0; i < digits.length; i++) {
			counts[digits[i]]++;
		}
		return counts;
	}
	
	/**
	 * Adds the digits in the number together.
	 * The number must be given as a String.
	 * @param toAdd
	 * @return The sum of the digits
	 */
	public static int digitAdd(String toAdd){
		int[] digits = digitSplit(toAdd);
		int sum=0;
		for(int c = 0; c< digits.length; c++){
			sum+=digits[c];
		}
		return sum;
	}
	
	/**
	 * Takes an int and reverses the order of the digits
	 * @param toFlip
	 * @return Flipped Number
	 */
	public static int flip(int toFlip){
		int[] digits = digitSplit(toFlip);
		int[] out = new int[digits.length];
		for(int x = 0; x< digits.length; x++){
			out[x]=digits[digits.length-1-x];
		}
		return recombine(out);
	}
	
	/**
	 * Takes a String and reverses the order of characters.
	 * @param toFlip
	 * @return Flipped String
	 */
	public static String flip(String toFlip){//uses and returns integers
		String out="";
		for(int x = (toFlip.length()-1); x>=0; x--){
			out=out+toFlip.charAt(x);
		}
		return out;
	}
	
	/**
	 * Takes a number as a String and returns an int array with each digit in its own spot
	 * @param number
	 * @return digit array
	 */
	public static int[] digitSplit(String number){
		int[] split = new int[number.length()];
		for(int x = 0; x<number.length(); x++){
			split[x]=(number.codePointAt(x))-48;
		}
		return split;
	}
	
	/**
	 * Takes a number as an int and returns an int array with each digit in its own spot
	 * @param n
	 * @return digit array
	 */
	public static int[] digitSplit(int n){//takes an int and puts each digit into its own place in an int array
		String number=Integer.toString(n);
		int[] split = new int[number.length()];
		for(int x = 0; x<number.length(); x++){
			split[x]=(number.codePointAt(x))-48;
		}
		return split;
	}
	
	/**
	 * Takes a number as a long and returns an int array with each digit in its own spot
	 * @param n
	 * @return digit array
	 */
	public static int[] digitSplit(long n){
		String number=Long.toString(n);
		int[] split = new int[number.length()];
		for(int x = 0; x<number.length(); x++){
			split[x]=(number.codePointAt(x))-48;
		}
		return split;
	}
	
	/**
	 * The inverse of digitSplit(), this method takes an int array and recombines it into a single int
	 * @param n
	 * @return recombined number
	 */
	public static int recombine(int[] n){
		String num ="";
		for(int i = 0; i<n.length; i++){
			num=num+Integer.toString(n[i]);
		}
		int combined= Integer.parseInt(num);
		return combined;
	}

	
	//real math stuff
	
	/**
	 * Takes a double and returns an int array with [0] as the numerator and [1] as the 
	 * denominator of a fraction representing that number
	 * @param convert
	 * @return numerator at [0], denominator at [1]
	 */
	public int[] toFrac(double convert){
		int whole = 0;
		double num=1;
		double denom=1;
		while(convert>1){
			whole++;
			convert--;		
		}
		num=convert;
		while(!((long)(num)<num+.001 && (long)(num)>num-.001)){
			num*=10;
			denom*=10;
		}
		num=(double)((long)num);
		denom=(double)((long)denom);
		
		for(int commonFactor=2; commonFactor<=num; commonFactor++){
			
			if(num%commonFactor==0 && denom%commonFactor==0 && JMath.isPrime(commonFactor)){
				num/=commonFactor;
				denom/=commonFactor;
				commonFactor=1;
			}
		}
		num+=whole*denom;
		int[] out = {(int)num, (int)denom};
		return out;
	}
	
	/**
	 * Tests if a given int is a perfect square
	 * @param test
	 * @return boolean
	 */
	public static boolean isPerfectSquare(int test){
		if(Math.ceil(Math.sqrt(test))==Math.sqrt(test)){
			return true;
		}
		else{
			return false;
		}
	}

	/**
	 * Tests if the given number is prime
	 * @param prime
	 * @return boolean
	 */
	public static boolean isPrime(int prime){// takes an integer, returns true if prime, else returns false
		if(prime==2){
			return true;
		}
		if(prime%2==0 || prime<2){
			return false;
		}
		else{
			for(int i=3; i<=Math.ceil(Math.sqrt(prime));i+=2){
				if(prime%i==0){
					return false;
				}
			}
			return true;
		}	
	}
	
	/**
	 * Tests if the given number is prime
	 * @param prime
	 * @return boolean
	 */
	public static boolean isPrime(long prime){// takes an integer, returns true if prime, else returns false
		if(prime==2){
			return true;
		}
		if(prime%2==0 || prime<2){
			return false;
		}
		else{
			for(int i=3; i<=Math.ceil(Math.sqrt(prime));i+=2){
				if(prime%i==0){
					return false;
				}
			}
			return true;
		}	
	}
	
	/**
	* Gives a list of primes up to the given number
	* @param number The number of primes to return
	* @return an array with the specified number of primes
	*/
	public static int[] listPrimes(int number){
		int[] primes = new int[number];
		int numPrimes = 0;
		int test = 2;
		while(numPrimes<number){
			if(isPrime(test)){
				primes[numPrimes]=test;
				numPrimes++;
			}
			test++;
		}
		return primes;
	}
	
	/**
	 * takes an int, n, and will return n! as long as n<21
	 * @param n
	 * @return n!
	 */
	public static long factorial(int n) {
        long fact = 1; 
        for (int i = 1; i <= n; i++) {
            fact *= i;
        }
        return fact;
	}

	/**
	 * performs a combination of the two given numbers
	 * @param n
	 * @param r
	 * @return nCr
	 */
	public static String combination(int n, int r){
		java.math.BigInteger larger = new java.math.BigInteger("1");
		java.math.BigInteger smaller = new java.math.BigInteger("1");
		java.math.BigInteger diff = new java.math.BigInteger("1");
		for(int i = 1; i<= n ; i++){
			larger=larger.multiply(new java.math.BigInteger(Integer.toString(i)));
		}
		for(int i = 1; i<= r ; i++){
			smaller=smaller.multiply(new java.math.BigInteger(Integer.toString(i)));
		}
		for(int i = 1; i<= (n-r) ; i++){
			diff=diff.multiply(new java.math.BigInteger(Integer.toString(i)));
		}
		smaller= smaller.multiply(diff);
		larger= larger.divide(smaller);
		return larger.toString();
	}
	
	/**
	 * Sorts the given array from least to greatest
	 * @param arrayName
	 * @return an ordered array
	 */
	public static int[] order(int [] arrayName){
		int temp;
		for (int i = 0; i < arrayName.length-1; i++)
		{
			if(arrayName[i] > arrayName[i+1])
			{
				temp=arrayName[i];
				arrayName[i]=arrayName[i+1];
				arrayName[i+1]=temp;
				i=-1;
			}
		}
		return arrayName;
	}
}
