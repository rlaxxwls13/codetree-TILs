import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final int INT_MIN = Integer.MIN_VALUE;
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[10];
        int ans = INT_MIN;

        for (int i = 0; i < 10; i++) {
            arr[i] = sc.nextInt();
            if(arr[i] > ans) {
                ans = arr[i];
            }
        }

        System.out.print(ans);
    }
}