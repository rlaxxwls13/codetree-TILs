import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[10];
        for(int i = 0; i < 10; i++) {
            arr[i] = sc.nextInt();
            }

        int sum = 0;
        double cnt = 10;
        for(int j = 0; j < 10; j++) {
            if (arr[j] >= 250) {
                cnt = j;
                break;
            }
            sum += arr[j];
        }

        double mean = sum / cnt;

        System.out.print(sum + " " + mean);
    }
}