import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int cnt = 0, sum;
        double avg;
        for (int i = 0; i < n; i++) {
            sum = 0;
            for (int j = 0; j < 4; j++) {
                sum += sc.nextInt();
            }
            avg = (double)sum / 4;
            if (avg >= 60) {
                cnt += 1;
                System.out.println("pass");
            } else {
                System.out.println("fail");
            }
        }
        System.out.println(cnt);
    }
}