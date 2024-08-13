public class MaximumFinder {

    // Method to find the maximum of three parameters
    public double maximum(double num1, double num2, double num3) {
        // Initialize max with the first number
        double max = num1;

        // Compare max with the second number
        if (num2 > max) {
            max = num2;
        }

        // Compare max with the third number
        if (num3 > max) {
            max = num3;
        }

        // Return the largest number
        return max;
    }

    public static void main(String[] args) {
        MaximumFinder finder = new MaximumFinder();
        // Test the maximum method with some values
        System.out.println("Maximum of 3.4, 5.2, and 1.9 is: " + finder.maximum(3.4, 5.2, 1.9));
        System.out.println("Maximum of 7.1, 2.3, and 5.5 is: " + finder.maximum(7.1, 2.3, 5.5));
    }
}
