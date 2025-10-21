import java.util.Scanner;

public class Main{
    public static final int MAX_N = 100;

    public static int n, s, e, cnt, endOfArray;
    public static int[] arr = new int[MAX_N];

    public static void cutArray(int s, int e) {
        int[] temp = new int[MAX_N];
        int tempIdx = 0;

        for (int i = 0; i < endOfArray; i++) {
            if (i < s || i > e) {
                temp[tempIdx++] = arr[i];
            }
        }

        for (int i = 0; i < tempIdx; i++) {
            arr[i] = temp[i];
        }

        endOfArray = tempIdx;
    }

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

        endOfArray = n;

        for (int i = 0; i < 2; i++) {
            s = sc.nextInt();
            e = sc.nextInt();
            cutArray(s - 1, e - 1);
        }

        System.out.println(endOfArray);
        for (int i = 0; i < endOfArray; i++) {
            System.out.println(arr[i]);
        }

    }
}