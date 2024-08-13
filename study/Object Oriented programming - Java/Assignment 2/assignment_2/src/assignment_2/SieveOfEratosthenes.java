package assignment_2;

public class SieveOfEratosthenes {
    public static void main(String[] args) {
        int size = 1000;
        boolean[] primes = new boolean[size];

        // Initialize all elements to true
        for (int i = 0; i < size; i++) {
            primes[i] = true;
        }

        // Apply Sieve of Eratosthenes algorithm
        for (int i = 2; i < Math.sqrt(size); i++) {
            if (primes[i]) {
                for (int j = i * i; j < size; j += i) {
                    primes[j] = false;
                }
            }
        }

        // Print all prime numbers between 2 and 999
        System.out.println("Prime numbers between 2 and 999 are:");
        for (int i = 2; i < size; i++) {
            if (primes[i]) {
                System.out.print(i + " ");
            }
        }
    }
}
