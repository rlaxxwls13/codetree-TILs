import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();

        int[] A = new int[n1];
        int[] B = new int[n2];
        for (int i = 0; i < n1; i++) {
            A[i] = sc.nextInt();
        }
        for (int i = 0; i < n2; i++) {
            B[i] = sc.nextInt();
        }

        boolean isSub = false;

        for (int i = 0; i < n1 - n2 + 1; i++) {
            for (int j = 0; j < n2; j++) {
                if (A[i + j] != B[j]) {
                    break;
                }
                if (j == n2 - 1) {
                    isSub = true;
                }
            }
        }

        if (isSub) {
            System.out.print("Yes");
        }
        else {
            System.out.print("No");
        }
    }
}