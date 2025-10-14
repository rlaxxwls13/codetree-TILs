import java.util.Scanner;

public class Main{
    public static final int MAX_N = 200;

    public static int n, t;
    public static int[] arr = new int[2 * MAX_N];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        t = sc.nextInt();

        for (int i = 0; i < 2 * n; i++)
            arr[i] = sc.nextInt();

        int tmp;

        for (int i = 0; i < t; i++) {
            tmp = arr[2*n - 1];
            for (int j = 2*n - 1; j >= 1; j--) {
                arr[j] = arr[j - 1];
            }
            arr[0] = tmp;
        }

        for (int i = 0; i < 2*n; i++) {
            System.out.print(arr[i] + " ");
            if (i == n - 1)
                System.out.println();
        }
    }
}