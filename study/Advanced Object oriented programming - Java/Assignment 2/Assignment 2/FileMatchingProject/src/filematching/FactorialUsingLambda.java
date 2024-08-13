package filematching;

import java.util.stream.IntStream;

public class FactorialUsingLambda {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Usage: java FactorialUsingLambda number");
            return;
        }

        int number = Integer.parseInt(args[0]);
        long factorial = calculateFactorial(number);
        System.out.println("Factorial of " + number + " is " + factorial);
    }

    public static long calculateFactorial(int number) {
        return IntStream.rangeClosed(1, number)
                        .asLongStream()
                        .reduce(1, (long a, long b) -> a * b);
    }
}
