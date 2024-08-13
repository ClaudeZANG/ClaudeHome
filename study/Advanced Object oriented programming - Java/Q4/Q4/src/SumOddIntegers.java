public class SumOddIntegers {
    public static void main(String[] args) {
        int sum = 0;
        // Loop through odd integers between 1 and 99
        for (int i = 1; i < 100; i += 2) {
            sum += i; // Add the odd integer to the sum
        }
        // Print the sum of odd integers
        System.out.println("Sum of odd integers between 1 and 99 is: " + sum);
    }
}
