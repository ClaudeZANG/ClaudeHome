import java.util.Scanner;

public class FindLargestNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double largestNumber = Double.NEGATIVE_INFINITY; // Initialize the largest number as the smallest possible value

        while (true) {
            // Prompt the user to enter a number
            System.out.print("Enter a number (or press Enter to finish): ");
            String userInput = scanner.nextLine(); // Read user input

            // Check if the user pressed Enter without entering a value
            if (userInput.isEmpty()) {
                break; // Exit the loop if the input is empty
            }

            // Convert the user input to a double
            double number = Double.parseDouble(userInput);

            // Check if the entered number is larger than the current largest number
            if (number > largestNumber) {
                largestNumber = number; // Update the largest number
            }
        }

        // Print the largest number inputted by the user
        System.out.printf("The largest number entered is: %.2f%n", largestNumber);
    }
}
