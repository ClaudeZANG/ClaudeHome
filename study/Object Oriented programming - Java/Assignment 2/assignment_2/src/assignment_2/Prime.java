package assignment_2;

import java.util.ArrayList;
import java.util.List;

public class Prime {
    public List<Integer> calculatePrime(int limit) throws IllegalArgumentException {
        if (limit < 2 || limit > 10000) {
            throw new IllegalArgumentException("Parameter must be between 2 and 10000");
        }

        boolean[] isPrime = new boolean[limit + 1];
        for (int i = 2; i <= limit; i++) {
            isPrime[i] = true;
        }

        for (int i = 2; i * i <= limit; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= limit; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= limit; i++) {
            if (isPrime[i]) {
                primes.add(i);
            }
        }

        return primes;
    }
}
