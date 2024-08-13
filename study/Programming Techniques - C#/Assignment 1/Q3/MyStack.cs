using System;

namespace StudentTeacherClassification
{
    public class MyStack<T>
    {
        private T[] elements;
        private int top;
        private int max;

        // Constructor
        public MyStack(int size)
        {
            elements = new T[size];
            top = -1;
            max = size;
        }

        // Push method
        public void Push(T element)
        {
            if (top == max - 1)
            {
                Console.WriteLine("Stack overflow!");
                return;
            }
            elements[++top] = element;
        }

        // Pop method
        public T Pop()
        {
            if (top == -1)
            {
                Console.WriteLine("Stack underflow!");
                return default(T);
            }
            return elements[top--];
        }

        // Peek method
        public T Peek()
        {
            if (top == -1)
            {
                Console.WriteLine("Stack is empty!");
                return default(T);
            }
            return elements[top];
        }

        // Check if stack is empty
        public bool IsEmpty()
        {
            return top == -1;
        }
    }
}
