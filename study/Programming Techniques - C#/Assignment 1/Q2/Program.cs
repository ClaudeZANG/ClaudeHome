using System;

namespace StudentTeacherClassification
{
    class Program
    {
        static void Main(string[] args)
        {
            // Create an instance of MyQueue
            MyQueue<int> queue = new MyQueue<int>();

            // Add elements to the queue
            queue.Enqueue(10);
            queue.Enqueue(20);
            queue.Enqueue(30);
            queue.Enqueue(40);
            queue.Enqueue(50);

            // Try to add an element to a full queue
            queue.Enqueue(60);

            // View the first element in the queue
            Console.WriteLine("First element in the queue: " + queue.Peek());

            // Remove and print all elements from the queue
            while (queue.Peek() != default(int))
            {
                Console.WriteLine(queue.Dequeue());
            }

            // Try to remove an element from an empty queue
            Console.WriteLine(queue.Dequeue());

            Console.ReadLine();
        }
    }
}
