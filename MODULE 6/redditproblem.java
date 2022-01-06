import java.util.Scanner;

public class redditproblem {
    static int arrayLength = scnr();
    static double[] doubleList = new double[arrayLength];

    public static int scnr() {
    	Scanner scnr = new Scanner(System.in);
    	arrayLength =scnr.nextInt();
    	scnr.close();
    	return arrayLength;
    }
    public static void main(String args[]){
		for (int i = 0; i < arrayLength; i++) {
			doubleList[i] = i+1;
		} 

		for (int i = 0; i < arrayLength; i++) {
			if (i < (arrayLength- 1)) {
				System.out.print(doubleList[i] + ", ");
			} 
			else {
				System.out.print(doubleList[i]);
			}
		}
	}
} 