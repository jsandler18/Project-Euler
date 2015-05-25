import java.util.ArrayList;
import java.util.Arrays;


public class Euler61 {
	//init polygon number lists
	ArrayList<Integer> triangles = genPolynomias(3);
	ArrayList<Integer> squares = genPolynomias(4);
	ArrayList<Integer> pents = genPolynomias(5);
	ArrayList<Integer> hexes = genPolynomias(6);
	ArrayList<Integer> hepts = genPolynomias(7);
	ArrayList<Integer> octs = genPolynomias(8);
	ArrayList[] lists = {triangles, squares, pents, hexes, hepts, octs};
	boolean[] visited = {true, false, false, false, false, false};
	int[] results = new int[6];
	
	Euler61() {

		for (Integer term : triangles) {
			if(search(term, 0)) {
				break;
			}
		}
		System.out.println(Arrays.toString(results));
		System.out.println(results[0]+results[1]+results[2]+results[3]+results[4]+results[5]);
	}
	
	/**
	 * tests if the two given terms can cycle
	 * @param term1
	 * @param term2
	 * @return
	 */
	private boolean cycles(int term1, int term2) {
		int[] t1 = JMath.digitSplit(term1);
		int[] t2 = JMath.digitSplit(term2);
		return t1[2] == t2[0] && t1[3] == t2[1];
	}
	
	/**
	 * gets the next polygon number for the given degree (3-8)
	 * @param n
	 * @param degree
	 * @return
	 */
	private int nextPolygonal(int n, int degree) {
		switch (degree) {
			case 3:
				return (n * (n + 1))/2;
			case 4:
				return (n * n);
			case 5:
				return (n * ((3 * n) - 1))/2;
			case 6:
				return (n * ((2 * n) - 1));
			case 7:
				return (n * ((5 * n) - 3))/2;
			case 8:
				return (n * ((3 * n) - 2));
			default:
				return 0;
		}
	}
	
	private ArrayList<Integer> genPolynomias (int degree) {
		ArrayList<Integer> p = new ArrayList<Integer>();
		int n = 0;
		int next = nextPolygonal(n, degree);
		while (next < 10000) {
			next = nextPolygonal(n, degree);
			if (next >= 1000) {
				p.add(next);
			}
			n++;
		}
		return p;
	}
	
	private int findNext(int term, ArrayList<Integer> numbers, int exclude) {
		int start = numbers.indexOf(exclude);
		int i = ((start == -1) ? 0 : start+1);
		for (; i < numbers.size(); i++) {
			if (cycles(term, numbers.get(i))) {
				return numbers.get(i);
			}
		}
		return 0;
	}

	private boolean search (int term, int resultIdx) {
		System.out.println(Arrays.toString(results));
		boolean allVisited = true;
		results[resultIdx] = term;
		for (int i = 0; i < lists.length; i++) {
			if (!visited[i]) {
				allVisited = false;
				visited[i]=true;
				int next = findNext(term, lists[i], 0);
				boolean nextFound = false;
				while (next != 0) {
					if (cycles(term, next)) {
						nextFound = search(next, resultIdx + 1);
					}
					if (nextFound) {
						return true;
					}
					else {
						next = findNext(term, lists[i], results[resultIdx+1]);
						results[resultIdx+1] = 0;
					}

				}
				visited[i] = false;
			}
		}
		if (allVisited) {
			//check if last cycles to first
			if (cycles(results[5], results[0])) {
				return true;
			}
		}
		return false;
	}
}
