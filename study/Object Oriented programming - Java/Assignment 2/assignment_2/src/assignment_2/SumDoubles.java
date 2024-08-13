package assignment_2;

public class SumDoubles {
    public static void main(String[] args) {
        // Initialize sum to 0.0
        double sum = 0.0;

        // Use enhanced for statement to sum the double values
        for (String arg : args) {
            // Convert the argument to double and add to sum
            sum += Double.parseDouble(arg);
        }

        // Print the sum
        System.out.printf("The sum of the double values is: %.2f%n", sum);
    }
}
