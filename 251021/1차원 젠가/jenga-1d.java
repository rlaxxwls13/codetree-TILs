import java.util.Scanner;

public class Main{
    public static final int MAX_N = 100;

    public static int n, s, e, cnt;
    public static int[] arr = new int[MAX_N];

    public static void removeBlock(int s, int e) {
        for(int i = s; i <= e; i++) {
            arr[i] = 0;
        }
    }

    public static void arrangeBlock() {
        int[] temp = new int[n];
        int tIdx = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] != 0) {
                temp[tIdx] = arr[i];
                tIdx++;
            }
        }
        cnt = tIdx;
        for (int i = tIdx; i < n; i++) {
            temp[i] = 0;
        }
        for (int i = 0; i < n; i++) {
            arr[i] = temp[i];
        }
    }

    public static void simulate(int s, int e) {
        removeBlock(s, e);
        arrangeBlock();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = 0; i < 2; i++) {
            s = sc.nextInt();
            e = sc.nextInt();
            simulate(s - 1, e - 1);
        }

        System.out.println(cnt);
        for (int i = 0; i < cnt; i++) {
            System.out.println(arr[i]);
        }

    }
}