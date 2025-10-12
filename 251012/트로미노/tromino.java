import java.util.Scanner;

public class Main {

    public static final int MAX_N = 200;

    public static int n, m;
    public static int[][] grid = new int[MAX_N][MAX_N];

    public static int[][][] shapes = new int[][][]{
        {{0, 1, 1},
        {0, 0, 1}},
        {{0, 0, -1},
        {0, 1, 1}},
        {{0, 0, 1},
        {0, 1, 0}},
        {{0, 0, 1},
        {0, 1, 1}},
        {{0, 0, 0},
        {0, 1, 2}},
        {{0, 1, 2},
        {0, 0, 0}}
    };

    public static int getMaxSum(int x, int y) {
        int currMax = 0;
        for (int i = 0; i < shapes.length; i++) {
            int sum = 0;
            for (int j = 0; j < 3; j++) {
                int nx = x + shapes[i][0][j];
                int ny = y + shapes[i][1][j];
                if(nx >= 0 && nx < n && ny >= 0 && ny < m)
                    sum += grid[nx][ny];
                else{
                    sum = 0;
                    break;
                }
            }
            currMax = Math.max(currMax, sum);
        }
        return currMax;
    }

/*
    public static int getBlock1Sum(int x, int y) {
        int blockSum1 = 0, blockSum2 = 0, blockSum3 = 0, blockSum4 = 0;
        if (x + 1 < n && y + 1 < m) {
            blockSum1 = grid[x][y] + grid[x+1][y] + grid[x+1][y+1];
            blockSum2 = grid[x][y] + grid[x+1][y] + grid[x][y+1];
            blockSum3 = grid[x][y] + grid[x][y+1] + grid[x+1][y+1];
        }
        if (x - 1 >= 0 && y + 1 < m)
            blockSum4 = grid[x][y] + grid[x-1][y+1] + grid[x][y+1];
        return Math.max(blockSum1, Math.max(blockSum2, Math.max(blockSum3, blockSum4)));
    }

    public static int getBlock2Sum(int x,int y) {
        int blockSum1 = 0, blockSum2 = 0;
        if (x + 2 < n)
            blockSum2 = grid[x][y] + grid[x+1][y] + grid[x+2][y];
        if (y + 2 < m)
            blockSum1 = grid[x][y] + grid[x][y+1] + grid[x][y+2];
        return Math.max(blockSum1, blockSum2);
    }
    */

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                grid[i][j] = sc.nextInt();
            }
        }

        int ans = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {

                //System.out.println(getBlock1Sum(i, j) + " " + getBlock2Sum(i, j));
                //ans = Math.max(ans, Math.max(getBlock1Sum(i, j), getBlock2Sum(i, j)));
                ans = Math.max(ans, getMaxSum(i, j));
            }
        }

        System.out.print(ans);
    }
}