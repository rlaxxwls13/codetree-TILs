import java.util.Scanner;

public class Main{
    public static final int MAX_N = 200;

    public static int n, t;
    public static int[] a = new int[MAX_N];
    public static int[] b = new int[MAX_N];
    public static int[] c = new int[MAX_N];
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        t = sc.nextInt();
        for (int i = 0; i < n; i++)
            a[i] = sc.nextInt();
        for (int i = 0; i < n; i++)
            b[i] = sc.nextInt();
        for (int i = 0; i < n; i++)
            c[i] = sc.nextInt();

        int temp1, temp2;
        
        for (int k = 0; k < t; k++) {
            temp1 = a[n-1];
            for (int i = n-1; i >= 1; i--)
                a[i] = a[i-1];
            a[0] = c[n-1];
            
            temp2 = b[n-1];
            for (int i = n-1; i >= 1; i--)
                b[i] = b[i-1];
            b[0] = temp1;

            for (int i = n-1; i >= 1; i--)
                c[i] = c[i-1];
            c[0] = temp2;

        }

        for (int i = 0; i < n; i++)
            System.out.print(a[i] + " ");
        System.out.println();
        for (int i = 0; i < n; i++)
            System.out.print(b[i] + " ");
        System.out.println();
        for (int i = 0; i < n; i++)
            System.out.print(c[i] + " ");
        
    }
}