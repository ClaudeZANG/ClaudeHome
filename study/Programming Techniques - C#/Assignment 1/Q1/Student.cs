using System;

namespace StudentTeacherClassification
{
    public class Student : Person
    {
        public Student(string name) : base(name)
        {
        }

        public void Study()
        {
            Console.WriteLine($"{Name} is studying.");
        }
    }
}
