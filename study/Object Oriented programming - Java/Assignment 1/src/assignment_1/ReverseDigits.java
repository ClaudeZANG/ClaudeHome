package assignment_1;

import java.util.Scanner;

public class ReverseDigits {
    // Method to reverse the digits of an integer
    public static int reverseNumber(int number) {
        int reversedNumber = 0;
        while (number != 0) {
            int digit = number % 10;
            reversedNumber = reversedNumber * 10 + digit;
            number /= 10;
        }
        return reversedNumber;
    }

    public static void main(String[] args) {
        // Create a Scanner object to read user input
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter an integer
        System.out.print("Please enter an integer: ");
        int number = scanner.nextInt();

        // Call the reverseNumber method and display the result
        int reversedNumber = reverseNumber(number);
        System.out.printf("The reversed number is: %d%n", reversedNumber);

        // Close the Scanner object
        scanner.close();
    }
}
