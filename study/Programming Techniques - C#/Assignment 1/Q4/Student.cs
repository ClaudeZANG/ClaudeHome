using System;

namespace StudentTeacherClassification
{
    public class Student : Person
    {
        public int Id { get; set; }
        public string CourseEnrolled { get; set; }

        public Student(string name, int id, string course) : base(name)
        {
            Id = id;
            CourseEnrolled = course;
        }

        public void Study()
        {
            Console.WriteLine($"{Name} is studying.");
        }

        public override string ToString()
        {
            return $"{Name} (ID: {Id}, Course: {CourseEnrolled})";
        }
    }
}
