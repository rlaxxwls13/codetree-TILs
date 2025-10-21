import java.util.Scanner;

public class Main{
    public static final int MAX_N = 100;
    public static final int MAX_M = 100;
    public static final int MAX_Q = 100;

    public static int n, m, q;
    public static int[][] grid = new int[MAX_N][MAX_M];
    public static int[][] avg = new int[MAX_N][MAX_M];
    public static int[][] queries = new int[MAX_Q][4];

    public static void shift(int r1, int c1, int r2, int c2) {

        int temp = grid[r1][c2];

        for (int i = c2; i > c1; i--) {
            grid[r1][i] = grid[r1][i-1];
        }
        for (int i = r1; i < r2; i++) {
            grid[i][c1] = grid[i+1][c1];
        }
        for (int i = c1; i < c2; i++) {
            grid[r2][i] = grid[r2][i+1];
        }
        for(int i = r2; i > r1; i--) {
            grid[i][c2] = grid[i-1][c2];
        }
        grid[r1+1][c2] = temp;

        /*
        int temp1 = grid[r1][c2];
        for (int i = c2; i >= c1+1; i--) {
            grid[r1][i] = grid[r1][i-1];
        }
        int temp2 = grid[r2][c2];
        for (int i = r2; i >= r1+2; i--) {
            grid[i][c2] = grid[i-1][c2];
        }
        grid[r1+1][c2] = temp1;
        int temp3 = grid[r2][c1];
        for (int i = c1; i <= c2-2; i++) {
            grid[r2][i] = grid[r2][i+1];
        }
        grid[r2][c2-1] = temp2;
        for (int i = r1; i <= r2-2; i++) {
            grid[i][c1] = grid[i+1][c1];
        }
        grid[r2-1][c1] = temp3;
        */
        /*
        System.out.println("회전");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++)
                System.out.print(grid[i][j] + " ");
            System.out.println();
        }
        System.out.println();
        */

        for (int i = r1; i <= r2; i++) {
            for (int j = c1; j <= c2; j++)
                avg[i][j] = getAvg(i, j);
        }

        copy(r1, c1, r2, c2);
/*
        System.out.println("평균");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++)
                System.out.print(grid[i][j] + " ");
            System.out.println();
        }
        System.out.println();
        */

    }

    public static void copy(int r1, int c1, int r2, int c2) {
        for (int i = r1; i <= r2; i++) {
            for (int j = c1; j <= c2; j++) {
                grid[i][j] = avg[i][j];
            }
        }
    }

    public static int getAvg(int r, int c) {
        int sum = 0;
        int cnt = 0;
        int[] dx = new int[]{0, -1, 0, 1, 0};
        int[] dy = new int[]{0, 0, 1, 0, -1};
        for (int i = 0; i < 5; i++) {
            int nx = r + dx[i];
            int ny = c + dy[i];
            if (inRange(nx, ny)){
                cnt++;
                sum += grid[nx][ny];
            }
        }
        return sum / cnt;
    }

    public static boolean inRange(int r, int c) {
        return 0 <= r && r < n && 0 <= c && c < m;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        q = sc.nextInt();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++)
                grid[i][j] = sc.nextInt();
        }
        
        for (int i = 0; i < q; i++) {
            for (int j = 0; j < 4; j++)
                queries[i][j] = sc.nextInt() - 1;
        }

        for (int i = 0; i < q; i++) {
            shift(queries[i][0], queries[i][1], queries[i][2], queries[i][3]);
        }


        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++)
                System.out.print(grid[i][j] + " ");
            System.out.println();
        }
    
    }
}