using System;
using System.Linq;

namespace CustomerManagement
{
    class Program
    {
        static void Main(string[] args)
        {
            Customer[] customers = new Customer[]
            {
                new Customer(1, "John", "Doe", new DateTime(1980, 1, 1)),
                new Customer(2, "Jane", "Smith", new DateTime(1990, 2, 2)),
                new Customer(3, "Bob", "Johnson", new DateTime(1985, 3, 3)),
                new Customer(4, "Alice", "Williams", new DateTime(1975, 4, 4)),
                new Customer(5, "Tom", "Brown", new DateTime(1965, 5, 5)),
                new Customer(6, "Sara", "Davis", new DateTime(2000, 6, 6)),
                new Customer(7, "Michael", "Miller", new DateTime(1995, 7, 7))
            };

            Console.WriteLine(GetCustomerById(customers, 3));
            Console.WriteLine(GetCustomerByFirstName(customers, "Sara"));
            SortCustomersByFirstName(customers);
        }

        static string GetCustomerById(Customer[] customers, int id)
        {
            var customer = customers.FirstOrDefault(c => c.Id == id);
            return customer != null ? $"{customer.FirstName} {customer.LastName}" : "Customer doesn’t exist";
        }

        static string GetCustomerByFirstName(Customer[] customers, string firstName)
        {
            var customer = customers.FirstOrDefault(c => c.FirstName.Equals(firstName, StringComparison.OrdinalIgnoreCase));
            return customer != null ? customer.DateOfBirth.ToString("d") : "Customer doesn’t exist";
        }

        static void SortCustomersByFirstName(Customer[] customers)
        {
            var sortedCustomers = customers.OrderBy(c => c.FirstName).ToArray();
            Console.WriteLine("Sorted Customers:");
            foreach (var customer in sortedCustomers)
            {
                Console.WriteLine($"{customer.FirstName} {customer.LastName}");
            }
        }
    }
}
