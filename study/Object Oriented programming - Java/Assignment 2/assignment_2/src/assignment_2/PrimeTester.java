package assignment_2;

import java.util.List;
import java.util.Scanner;

public class PrimeTester {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Prime prime = new Prime();

        try {
            System.out.print("Enter a number to find all prime numbers up to that limit: ");
            int limit = scanner.nextInt();

            List<Integer> primes = prime.calculatePrime(limit);
            System.out.println("Prime numbers up to " + limit + ": " + primes);
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
}
