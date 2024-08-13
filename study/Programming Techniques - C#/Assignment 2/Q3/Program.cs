using System;

namespace FibonacciSequence
{
    class Program
    {
        static void Main(string[] args)
        {
            Fibonacci fib = new Fibonacci(5);
            Console.WriteLine($"Fibonacci({fib.Value}) = {fib}");
            fib++;
            Console.WriteLine($"Fibonacci({fib.Value}) = {fib}");
            fib = fib + 3;
            Console.WriteLine($"Fibonacci({fib.Value}) = {fib}");
        }
    }
}
