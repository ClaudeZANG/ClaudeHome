public class PowerCalculation {
    public static void main(String[] args) {
        double base = 2.5;
        int exponent = 3;
        double result = 1.0;

        // Loop to calculate the power
        for (int i = 0; i < exponent; i++) {
            result *= base; // Multiply the base
        }

        // Print the result of the power calculation
        System.out.println("2.5 raised to the power of 3 is: " + result);
    }
}
