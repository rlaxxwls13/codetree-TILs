import java.util.Scanner;

public class Main{
    public static final int MAX_N = 100;

    public static int n, m, q, r;
    public static char d;
    public static int[][] grid = new int[MAX_N][MAX_N];


    public static void shiftRight(int r) {
        //오른쪽으로 전이
        int temp = grid[r][m-1];

        for(int i = m-1; i >= 1; i--) {
            grid[r][i] = grid[r][i-1];
        }
        grid[r][0] = temp;
    }

    public static void shiftLeft(int r) {
        //왼쪽으로 전이
        int temp = grid[r][0];

        for(int i = 0; i <= m-2; i++) {
            grid[r][i] = grid[r][i+1];
        }
        grid[r][m-1] = temp;
    }

    public static boolean canShift(int r1, int r2) {
        boolean result = false;
        for(int i = 0; i < m; i++) {
            if (grid[r1][i] == grid[r2][i])
                result = true;
        }
        return result;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        q = sc.nextInt();

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++)
                grid[i][j] = sc.nextInt();
        }

        for(int i = 0; i < q; i++){
            r = sc.nextInt() - 1;
            d = sc.next().charAt(0);
            char upperD, lowerD;
            
            //첫 번째 행 Shift
            if (d == 'R') {
                upperD = 'L';
                lowerD = 'L';
                shiftLeft(r);
            } else {
                upperD = 'R';
                lowerD = 'R';
                shiftRight(r);
            }
                
            //위로 전이
            for (int row = r; row >= 1; row--) {
                if(!canShift(row, row-1))
                    break;

                if (upperD == 'R'){
                    shiftLeft(row-1);
                    upperD = 'L';
                } else if (upperD == 'L'){
                    shiftRight(row-1);
                    upperD = 'R';
                }
            }

            //아래로 전이
            for (int row = r; row <= n-2; row++) {
                if(!canShift(row, row+1)) 
                    break;

                if (lowerD == 'R'){
                    shiftLeft(row+1);
                    lowerD = 'L';
                } else if (lowerD == 'L'){
                    shiftRight(row+1);
                    lowerD = 'R';
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(grid[i][j] + " ");
            }
            System.out.println();
        }
        
    }
}