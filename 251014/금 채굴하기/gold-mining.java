import java.util.Scanner;

public class Main{

    public static final int MAX_N = 20;
    public static int n, m, k;
    public static int[][] grid = new int[MAX_N][MAX_N];

    public static int getNumOfGold(int k, int x, int y) {
        //1. 격자 안에 포함된 점인지
        //2. 마름모에 포함된 점인지
        int numOfGold = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (Math.abs(x-i) + Math.abs(y-j) <= k) {
                    if(grid[i][j] == 1)
                        numOfGold += 1;
                }
            }
        }
        return numOfGold;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = sc.nextInt();
            }
        }

        int ans = 0;
        for (int k = 0; k < 2*n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (getNumOfGold(k, i, j) * m >= Math.pow(k, 2) + Math.pow(k+1, 2)) {
                        ans = Math.max(ans, getNumOfGold(k, i, j));
                    }
                }
            }
        }
        System.out.print(ans);
    }
}