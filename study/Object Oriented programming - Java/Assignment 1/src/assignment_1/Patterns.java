package assignment_1;

public class Patterns {
    public static void main(String[] args) {
        // Pattern 1
        for (int i = 1; i <= 10; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        System.out.println(); // Add a blank line between patterns

        // Pattern 2
        for (int i = 10; i >= 1; i--) {
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        System.out.println(); // Add a blank line between patterns

        // Pattern 3
        for (int i = 10; i >= 1; i--) {
            for (int j = 10; j > i; j--) {
                System.out.print(" ");
            }
            for (int k = 1; k <= i; k++) {
                System.out.print("*");
            }
            System.out.println();
        }

        System.out.println(); // Add a blank line between patterns

        // Pattern 4
        for (int i = 1; i <= 10; i++) {
            for (int j = 10; j > i; j--) {
                System.out.print(" ");
            }
            for (int k = 1; k <= i; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
