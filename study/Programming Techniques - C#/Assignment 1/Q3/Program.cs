using System;

namespace StudentTeacherClassification
{
    class Program
    {
        static void Main(string[] args)
        {
            // Read input sequence of characters
            Console.Write("Enter a sequence of characters: ");
            string input = Console.ReadLine();

            // Create a stack with size equal to input length
            MyStack<char> stack = new MyStack<char>(input.Length);

            // Push each character of the input onto the stack
            foreach (char ch in input)
            {
                stack.Push(ch);
            }

            // Pop each character from the stack and print to reverse the sequence
            Console.Write("Reversed sequence: ");
            while (!stack.IsEmpty())
            {
                Console.Write(stack.Pop());
            }

            Console.ReadLine();
        }
    }
}
