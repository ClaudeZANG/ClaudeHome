package assignment_1;

import java.util.Scanner;
import java.util.Random;

public class GuessNumber {
    public static void main(String[] args) {
        // Generate a random number between 1 and 1000
        Random random = new Random();
        int numberToGuess = random.nextInt(1000) + 1;

        // Create a Scanner object to read user input
        Scanner scanner = new Scanner(System.in);
        boolean guessed = false;

        while (!guessed) {
            // Prompt the user to guess the number
            System.out.print("Guess a number between 1 and 1000: ");
            int userGuess = scanner.nextInt();

            // Check the user's guess
            if (userGuess == numberToGuess) {
                System.out.println("Congratulations. You guessed the number!");
                guessed = true;
            } else if (userGuess < numberToGuess) {
                System.out.println("Too low. Try again.");
            } else {
                System.out.println("Too high. Try again.");
            }
        }

        // Close the Scanner object
        scanner.close();
    }
}
