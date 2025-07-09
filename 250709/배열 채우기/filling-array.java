import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int[] arr = new int[10];
        int cnt = 9;
        for (int i = 0; i < 10; i++) {
            arr[i] = sc.nextInt();
            if (arr[i] == 0) {
                cnt = i - 1;
                break;
            }
        }

        for (int i = cnt; i >= 0; i--) {
            System.out.print(arr[i] + " ");
        }
    }
}