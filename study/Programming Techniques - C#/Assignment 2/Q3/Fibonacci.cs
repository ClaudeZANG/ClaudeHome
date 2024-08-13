using System;

namespace FibonacciSequence
{
    public class Fibonacci
    {
        public int Value { get; set; }

        public Fibonacci(int value)
        {
            Value = value;
        }

        public static Fibonacci operator ++(Fibonacci fib)
        {
            return new Fibonacci(GetFibonacci(fib.Value + 1));
        }

        public static Fibonacci operator +(Fibonacci fib, int n)
        {
            return new Fibonacci(GetFibonacci(fib.Value + n));
        }

        private static int GetFibonacci(int n)
        {
            if (n <= 1) return n;
            int a = 0, b = 1, c = 0;
            for (int i = 2; i <= n; i++)
            {
                c = a + b;
                a = b;
                b = c;
            }
            return c;
        }

        public override string ToString()
        {
            return Value.ToString();
        }
    }
}
