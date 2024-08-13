package assignment_1;

import java.util.Scanner;

public class GasMileage {
    public static void main(String[] args) {
        // Initialize variables
        int totalMiles = 0;
        int totalGallons = 0;
        Scanner scanner = new Scanner(System.in);

        while (true) {
            // Prompt the user to enter miles driven
            System.out.print("Enter miles driven (-1 to quit): ");
            int miles = scanner.nextInt();

            if (miles == -1) {
                break;
            }

            // Prompt the user to enter gallons used
            System.out.print("Enter gallons used: ");
            int gallons = scanner.nextInt();

            // Calculate and display the miles per gallon for this trip
            double milesPerGallon = (double) miles / gallons;
            System.out.printf("Miles per gallon for this trip: %.2f%n", milesPerGallon);

            // Add the miles and gallons to the totals
            totalMiles += miles;
            totalGallons += gallons;
        }

        // Calculate and display the combined miles per gallon
        if (totalGallons != 0) {
            double totalMilesPerGallon = (double) totalMiles / totalGallons;
            System.out.printf("Total miles per gallon: %.2f%n", totalMilesPerGallon);
        } else {
            System.out.println("No data entered.");
        }

        // Close the scanner
        scanner.close();
    }
}
