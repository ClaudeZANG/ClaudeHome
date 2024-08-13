// Q1
// Pseudocode:
// 1. Define a class called Car.
// 2. Inside the Car class, define a method named Start which prints "Car started!".
// 3. In the main program:
//    a. Create an instance of the Car class.
//    b. Call the Start method on the Car instance.

using System;

public class Car
{
    public void Start()
    {
        Console.WriteLine("Car started!");
    }
}

using System;

class Program
{
    static void Main()
    {
        // Create an instance of the Car class
        Car myCar = new Car();
        
        // Call the Start method on the Car instance
        myCar.Start();
    }
}


// Q2

using System;

public class Program
{
    // Define a struct to store employee data
    public struct Employee
    {
        public string Name;
        public struct DateOfBirth
        {
            public int Day;
            public int Month;
            public int Year;
        }
        public DateOfBirth DOB;
    }

    static void Main()
    {
        // Create an array to store employee data
        Employee[] employees = new Employee[2];

        // Populate the array with test data
        employees[0].Name = "H.Rana";
        employees[0].DOB.Day = 5;
        employees[0].DOB.Month = 2;
        employees[0].DOB.Year = 58;

        employees[1].Name = "S.Mathur";
        employees[1].DOB.Day = 4;
        employees[1].DOB.Month = 8;
        employees[1].DOB.Year = 59;

        // Display the data stored in the array
        Console.WriteLine("Employee Data:");
        foreach (Employee emp in employees)
        {
            Console.WriteLine($"Name: {emp.Name}");
            Console.WriteLine($"Date of Birth: {emp.DOB.Day}/{emp.DOB.Month}/{emp.DOB.Year}");
            Console.WriteLine();
        }
    }
}

// Q3
// Pseudocode:
// 1. Check if both arrays have a length greater than 0.
// 2. If true, check if the first element of array1 equals the first element of array2.
// 3. If true, return true.
// 4. If false, check if the last element of array1 equals the last element of array2.
// 5. If true, return true.
// 6. Otherwise, return false.

using System;

class Program
{
    static void Main()
    {
        // Test arrays
        int[] array1 = { 1, 2, 2, 3, 3, 4, 5, 6, 5, 7, 7, 7, 8, 8, 1 };
        int[] array2 = { 1, 2, 2, 3, 3, 4, 5, 6, 5, 7, 7, 7, 8, 8, 5 };

        // Check if the first or last element of the arrays are equal
        bool result = CheckFirstOrLastElementsEqual(array1, array2);

        // Print the result
        Console.WriteLine(result);
    }

    // Method to check if the first or last element of two arrays are equal
    static bool CheckFirstOrLastElementsEqual(int[] array1, int[] array2)
    {
        // Check if arrays are not empty
        if (array1.Length > 0 && array2.Length > 0)
        {
            // Check if the first element of array1 equals the first element of array2
            if (array1[0] == array2[0])
            {
                return true;
            }

            // Check if the last element of array1 equals the last element of array2
            if (array1[array1.Length - 1] == array2[array2.Length - 1])
            {
                return true;
            }
        }

        return false;
    }
}



// Q4
// Pseudocode:
// 1. Initialize two pointers, start and end, pointing to the start and end of the string respectively.
// 2. While start < end:
//    a. If the character at start does not equal the character at end, return false.
//    b. Increment start and decrement end.
// 3. If the loop completes without returning false, return true.

using System;

class Program
{
    static void Main()
    {
        // Test cases
        Console.WriteLine(IsPalindrome("aba"));   // true
        Console.WriteLine(IsPalindrome("abcd"));  // false
    }

    // Function to check if a string is a palindrome
    static bool IsPalindrome(string str)
    {
        // Initialize pointers
        int start = 0;
        int end = str.Length - 1;

        // Iterate over the string
        while (start < end)
        {
            // Compare characters at start and end positions
            if (str[start] != str[end])
            {
                return false; // Not a palindrome
            }

            // Move pointers
            start++;
            end--;
        }

        return true; // Palindrome
    }
}


// Q5
// Pseudocode:
// Function add(numbers: array of integers) -> integer
//     sum = 0
//     for each number in numbers
//         sum = sum + number
//     return sum

// using System;

// This pseudocode describes the steps performed by the add() function:

// Initialize a variable sum to store the sum of numbers.
// Iterate through each number in the numbers array.
// Add each number to the sum.
// Return the sum as the result.

class Program
{
    static void Main()
    {
        // Test the add() function with different numbers of parameters
        Console.WriteLine(add(1, 2, 3));                // Output: 6
        Console.WriteLine(add(5, 10, 15, 20));          // Output: 50
        Console.WriteLine(add(2, 4, 6, 8, 10, 12, 14)); // Output: 56
        Console.WriteLine(add(3, 7));                   // Output: 10
    }

    // Function to add any number of integer parameters
    static int add(params int[] numbers)
    {
        int sum = 0;

        // Loop through each number in the 'numbers' array and add it to the sum
        foreach (int num in numbers)
        {
            sum += num;
        }

        return sum;
    }
}


// Q6
// Algorithm (Pseudocode):
// Read the number of elements to be stored in the array from the user.
// Create the first array with the specified number of elements.
// Read elements into the first array.
// Create the second array with the same size as the first array.
// Copy elements from the first array to the second array.
// Display the elements stored in the first array.
// Display the elements copied into the second array.

using System;

class Program
{
    static void Main()
    {
        // Step 1: Read the number of elements from the user
        Console.Write("Input the number of elements to be stored in the array: ");
        int numElements = int.Parse(Console.ReadLine());

        // Step 2: Create the first array
        int[] firstArray = new int[numElements];

        // Step 3: Read elements into the first array
        Console.WriteLine($"Input {numElements} elements in the array:");
        for (int i = 0; i < numElements; i++)
        {
            Console.Write($"element - {i} : ");
            firstArray[i] = int.Parse(Console.ReadLine());
        }

        // Step 4: Create the second array with the same size as the first array
        int[] secondArray = new int[numElements];

        // Step 5: Copy elements from the first array to the second array
        Array.Copy(firstArray, secondArray, numElements);

        // Step 6: Display the elements stored in the first array
        Console.WriteLine("The elements stored in the first array are :");
        Console.WriteLine(string.Join(" ", firstArray));

        // Step 7: Display the elements copied into the second array
        Console.WriteLine("The elements copied into the second array are :");
        Console.WriteLine(string.Join(" ", secondArray));
    }
}



// Q7
//Algorithm (Pseudocode):
// Read the size of the array from the user.
// Create an array of the specified size.
// Read elements into the array.
// Sort the array in ascending order.
// Reverse the array.
// Display the sorted array in descending order.

using System;

class Program
{
    static void Main()
    {
        // Step 1: Read the size of the array from the user
        Console.Write("Input the size of array: ");
        int size = int.Parse(Console.ReadLine());

        // Step 2: Create the array
        int[] arr = new int[size];

        // Step 3: Read elements into the array
        Console.WriteLine($"Input {size} elements in the array:");
        for (int i = 0; i < size; i++)
        {
            Console.Write($"element - {i} : ");
            arr[i] = int.Parse(Console.ReadLine());
        }

        // Step 4: Sort the array in ascending order
        Array.Sort(arr);

        // Step 5: Reverse the array
        Array.Reverse(arr);

        // Step 6: Display the sorted array in descending order
        Console.WriteLine("Elements of the array in sorted descending order:");
        foreach (int num in arr)
        {
            Console.Write(num + " ");
        }
    }
}
