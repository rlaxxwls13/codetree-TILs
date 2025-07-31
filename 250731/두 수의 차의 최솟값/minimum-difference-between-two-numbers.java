import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final int MAX_INT = Integer.MAX_VALUE;
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int min = MAX_INT;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (Math.abs(i - j) < min) {
                    min = Math.abs(i - j);
                }
            }
        }
        
        System.out.print(min);
    }
}