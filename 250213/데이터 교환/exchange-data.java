public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        int a = 5, b = 6, c = 7;
        int tmp = c;
        c = b;
        b = a;
        a = tmp;

        System.out.print(a + "\n" + b + "\n" + c);
    }
}