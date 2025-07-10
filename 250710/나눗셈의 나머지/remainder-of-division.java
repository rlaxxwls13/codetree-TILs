import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int[] remain = new int[B];
        while(A > 1) {
            remain[A % B]++;
            A /= B;
        }

        int sum = 0;
        for(int i = 0; i < B; i++) {
            sum += remain[i] * remain[i];
        }

        System.out.print(sum);
    }
}