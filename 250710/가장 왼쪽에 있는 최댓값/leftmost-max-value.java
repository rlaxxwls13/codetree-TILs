import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];

        for(int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int end_idx = n;
        while (end_idx > 0) {
            int max_idx = 0;
            int max = arr[0];

            for(int i = 1; i < end_idx; i++) {
                if(arr[i] > max) {
                    max = arr[i];
                    max_idx = i;
                }
            }
            end_idx = max_idx;
            System.out.print((max_idx + 1) + " ");
        }
    }
}