package assignment_1;

import java.util.Scanner;

public class CharacterToInteger {
    public static void main(String[] args) {
        // Create a Scanner object to read user input
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter a character
        System.out.print("Please enter a character: ");
        char character = scanner.next().charAt(0);

        // Convert the character to its integer equivalent
        int integerEquivalent = (int) character;

        // Output the character and its integer equivalent
        System.out.printf("The character '%c' has the value %d%n", character, integerEquivalent);

        // Close the Scanner object
        scanner.close();
    }
}
