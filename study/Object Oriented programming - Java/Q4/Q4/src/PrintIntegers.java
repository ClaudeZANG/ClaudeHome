public class PrintIntegers {
    public static void main(String[] args) {
        // Loop through integers from 1 to 20
        for (int i = 1; i <= 20; i++) {
            System.out.print(i + " ");
            // Print a new line after every 5 integers
            if (i % 5 == 0) {
                System.out.println();
            }
        }
    }
}
