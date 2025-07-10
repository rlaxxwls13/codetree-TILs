import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        char[] hasSympton = new char[3];
        int[] temp = new int[3];
        for (int i = 0; i < 3; i++) {
            hasSympton[i] = sc.next().charAt(0);
            temp[i] = sc.nextInt();
        }

        int[] level = new int[4];
        for (int i = 0; i < 3; i++) {
            if (hasSympton[i] == 'Y') {
                if (temp[i] >= 37) {
                    level[0]++;
                } else {
                    level[2]++;
                }
            } else {
                if (temp[i] >= 37) {
                    level[1]++;
                } else {
                    level[3]++;
                }
            }
        }

        for (int i = 0; i < 4; i++) {
            System.out.print(level[i] + " ");
        }
        if (level[0] >= 2) {
            System.out.print("E");
        }

    }
}