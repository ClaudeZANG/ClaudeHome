import java.util.Scanner;

public class DisplayAsterisks {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] numbers = new int[5];

        // Read five numbers between 1 and 30
        for (int i = 0; i < 5; i++) {
            int number;
            // Validate the input to be between 1 and 30
            do {
                System.out.print("Enter a number between 1 and 30: ");
                number = scanner.nextInt();
            } while (number < 1 || number > 30);

            numbers[i] = number; // Store the number in the array
        }

        // Display the bars of asterisks
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < numbers[i]; j++) {
                System.out.print("*"); // Print asterisk
            }
            System.out.println(); // Move to the next line after each number
        }
    }
}
