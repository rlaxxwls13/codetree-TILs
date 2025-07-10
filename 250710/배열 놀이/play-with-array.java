import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int q = sc.nextInt();

        int[] element = new int[n];
        for (int i = 0; i < n; i++) {
            element[i] = sc.nextInt();
        }
        sc.nextLine();

        for (int i = 0; i < q; i++) {
            String[] strQuery = sc.nextLine().split(" ");
            int[] query = new int[strQuery.length];
            for (int j = 0; j < query.length; j++) {
                query[j] = Integer.parseInt(strQuery[j]);
            }
            if (query[0] == 1) {
                System.out.println(element[query[1] - 1]);
            } else if (query[0] == 2) {
                int idx = 0;
                for (int k = 0; k < n; k++) {
                    if (element[k] == query[1]) {
                        idx = k + 1;
                        break;
                    }
                }
                System.out.println(idx);
            } else {
                for (int k = query[1] - 1; k <= query[2] - 1; k++) {
                    System.out.print(element[k] + " ");
                }
                System.out.println();
            }
        }
    }
}