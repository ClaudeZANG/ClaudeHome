using System;

namespace StudentTeacherClassification
{
    class Program
    {
        static void Main(string[] args)
        {
            Person[] people = new Person[3];

            people[0] = new Teacher("Juan");
            people[1] = new Student("Sara");
            people[2] = new Student("Carlos");

            foreach (var person in people)
            {
                if (person is Teacher)
                {
                    ((Teacher)person).Explain();
                }
                else if (person is Student)
                {
                    ((Student)person).Study();
                }
            }

            Console.ReadLine();
        }
    }
}
