package assignment_1;

import java.util.Scanner;

public class OddOrEven {
    public static void main(String[] args) {
        // Create a Scanner object to read user input
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter an integer
        System.out.print("Please enter an integer: ");
        int number = scanner.nextInt();

        // Check if the integer is odd or even and output the result
        if (number % 2 == 0) {
            System.out.println("The number is even");
        } else {
            System.out.println("The number is odd");
        }

        // Close the Scanner object
        scanner.close();
    }
}
