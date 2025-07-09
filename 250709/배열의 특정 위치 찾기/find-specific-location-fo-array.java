import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[10];
        for (int i = 0; i < 10; i++) {
            arr[i] = sc.nextInt();
        }
        int evenSum = 0, thirdSum = 0, thirdCnt = 0;
        for (int i = 0; i < 10; i++) {
            if (i % 2 != 0) {
                evenSum += arr[i];
            }
            if ((i+1) % 3 == 0) {
                thirdCnt += 1;
                thirdSum += arr[i];
            }
        }
        double thirdAvg = (double)thirdSum/thirdCnt;
        //System.out.print(evenSum + " " + thirdAvg);
        System.out.printf("%d %.1f", evenSum, thirdAvg);
    }
}