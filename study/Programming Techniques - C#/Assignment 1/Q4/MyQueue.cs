using System;
using System.Collections.Generic;

namespace StudentTeacherClassification
{
    public class MyQueue<T>
    {
        private List<T> elements;

        public MyQueue()
        {
            elements = new List<T>();
        }

        public void Enqueue(T item)
        {
            elements.Add(item);
        }

        public T Dequeue()
        {
            if (elements.Count > 0)
            {
                T item = elements[0];
                elements.RemoveAt(0);
                return item;
            }
            else
            {
                throw new InvalidOperationException("Queue is empty!");
            }
        }

        public T Peek()
        {
            if (elements.Count > 0)
            {
                return elements[0];
            }
            else
            {
                throw new InvalidOperationException("Queue is empty!");
            }
        }

        public List<T> GetAll()
        {
            return elements;
        }

        public int Count => elements.Count;
    }
}
