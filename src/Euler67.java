import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Arrays;
import java.util.Scanner;


public class Euler67 {
	public Euler67() {
		int [][] numbers = readTriangle();
		for (int i = 98; i >= 0; i--) {
			for (int j = 0; j <  numbers[i].length; j++) {
				int left = numbers[i+1][j];
				int right = numbers[i+1][j+1];
				
				numbers[i][j] += left > right ? left : right;
			}
		}
		System.out.println(numbers[0][0]);
		
	}
	
	private int[][] readTriangle () {
		int [][] numbers = new int[100][];
		try {
			Scanner reader = new Scanner(new FileReader("C:\\Users\\Jake\\Desktop\\programming\\Project Euler\\p067_triangle.txt"));
			for (int i = 0; i < 100; i++) {
				numbers[i] = new int[i+1];
				for(int j = 0; j < i+1; j++) {
					numbers[i][j] = reader.nextInt();
				}
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return numbers;
	}
}
