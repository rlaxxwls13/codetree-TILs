import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.

        Scanner sc = new Scanner(System.in);

        sc.useDelimiter(":");

        int h = sc.nextInt(), m = sc.nextInt();

        System.out.printf("%d:%d", h + 1, m);
    }
}
