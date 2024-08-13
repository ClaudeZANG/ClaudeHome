using System;

namespace StudentTeacherClassification
{
    public class MyQueue<T>
    {
        private T[] elements;
        private int front;
        private int rear;
        private int max;
        private int count;

        public MyQueue(int size = 5)
        {
            elements = new T[size];
            front = 0;
            rear = -1;
            max = size;
            count = 0;
        }

        public void Enqueue(T item)
        {
            if (count == max)
            {
                Console.WriteLine("Queue is full!");
                return;
            }

            rear = (rear + 1) % max;
            elements[rear] = item;
            count++;
        }

        public T Peek()
        {
            if (count == 0)
            {
                Console.WriteLine("Queue is empty!");
                return default(T);
            }

            return elements[front];
        }

        public T Dequeue()
        {
            if (count == 0)
            {
                Console.WriteLine("Queue is empty!");
                return default(T);
            }

            T item = elements[front];
            front = (front + 1) % max;
            count--;
            return item;
        }
    }
}
