import java.util.Scanner;

public class Main {

    public static final int MAX_N = 100;
    public static int n, m;
    public static int[][] grid = new int[MAX_N][MAX_N];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                grid[i][j] = sc.nextInt();
        }

        int ans = 0;
        int prev, streak;

        for (int i = 0; i < n; i++) {
            prev = 0; streak = 1;
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == prev)
                    streak += 1;
                else {
                    streak = 1;
                    prev = grid[i][j];
                }
                //System.out.println(i + " " + j + " " + streak);
                if (streak == m) {
                    ans += 1;
                    break;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            prev = 0; streak = 1;
            for (int j = 0; j < n; j++) {
                if (grid[j][i] == prev)
                    streak += 1;
                else {
                    streak = 1;
                    prev = grid[j][i];
                }

               //System.out.println(i + " " + j + " " + streak);
                if (streak == m) {
                    ans += 1;
                    break;
                }
            }
        }
        System.out.print(ans);
    }
}