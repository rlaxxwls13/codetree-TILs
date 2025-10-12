import java.util.Scanner;

public class Main {

    public static final int MAX_N = 100;
    public static int n, m;
    public static int[][] grid = new int[MAX_N][MAX_N];
    public static int[] seq = new int[MAX_N];

    public static int isHappySequence() {
        int streak = 1, maxStreak = 1;
        for (int i = 1; i < n; i++) {
            if (seq[i] == seq[i-1])
                streak += 1;
            else
                streak = 1;
            maxStreak = Math.max(streak, maxStreak);
        }
        if (maxStreak >= m)
            return 1;
        else
            return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                grid[i][j] = sc.nextInt();
        }

        int ans = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                seq[j] = grid[i][j];
            }
            ans += isHappySequence();
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                seq[j] = grid[j][i];
            }
            ans += isHappySequence();
        }
        /*
        int streak;

        for (int i = 0; i < n; i++) {
            streak = 1;
            for (int j = 1; j < n; j++) {
                if (grid[i][j] == grid[i][j-1])
                    streak += 1;
                else {
                    streak = 1;
                }
                //System.out.println(i + " " + j + " " + streak);
                if (streak == m) {
                    ans += 1;
                    break;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            streak = 1;
            for (int j = 1; j < n; j++) {
                if (grid[j][i] == grid[j-1][i])
                    streak += 1;
                else {
                    streak = 1;
                }

               //System.out.println(i + " " + j + " " + streak);
                if (streak == m) {
                    ans += 1;
                    break;
                }
            }
        }
        */

        System.out.print(ans);
    }
}