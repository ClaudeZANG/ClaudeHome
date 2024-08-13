using System;

namespace StudentTeacherClassification
{
    public class Teacher : Person
    {
        public Teacher(string name) : base(name) { }

        public void Explain()
        {
            Console.WriteLine($"{Name} is explaining.");
        }
    }
}
