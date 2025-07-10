import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        final int MAX_INT = Integer.MAX_VALUE;

        int n = sc.nextInt();
        int min = MAX_INT;
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            if (arr[i] < min) {
                min = arr[i];
            }
        }

        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] == min) {
                cnt++;
            }
        }

        System.out.print(min + " " + cnt);
    }
}