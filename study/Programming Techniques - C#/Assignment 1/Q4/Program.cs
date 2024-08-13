using System;
using System.Collections.Generic;
using System.Linq;

namespace StudentTeacherClassification
{
    class Program
    {
        static void Main(string[] args)
        {
            // Step 1: Create and populate the queue with students
            MyQueue<Student> studentQueue = new MyQueue<Student>();

            studentQueue.Enqueue(new Student("John", 1, "Math"));
            studentQueue.Enqueue(new Student("Sara", 2, "Physics"));
            studentQueue.Enqueue(new Student("Alex", 3, "Biology"));
            studentQueue.Enqueue(new Student("Emma", 4, "Chemistry"));
            studentQueue.Enqueue(new Student("Michael", 5, "Literature"));

            // Step 2: Sort the students by name using lambda expression
            var sortedStudents = studentQueue.GetAll().OrderBy(s => s.Name).ToList();

            // Step 3: Print the sorted students
            Console.WriteLine("Sorted Students:");
            foreach (var student in sortedStudents)
            {
                Console.WriteLine(student);
            }

            // Step 4: Dequeue and print students
            Console.WriteLine("Dequeue and Print Students:");
            while (studentQueue.Count > 0)
            {
                Console.WriteLine(studentQueue.Dequeue());
            }

            Console.ReadLine();
        }
    }
}
