import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int min = arr[1] - arr[0];

        for (int i = 1; i < n - 1; i++) {
            int diff = arr[i + 1] - arr[i];
            if (min > diff) {
                min = diff;
            }
        }

        System.out.print(min);
        
    }
}