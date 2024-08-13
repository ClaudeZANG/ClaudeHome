// Q1
// # Pseudocode:
// 1. Read the mathematical expressions.
// 2. Evaluate each expression:
//    a. Use appropriate arithmetic operators and parentheses to ensure correct order of operations.
// 3. Print the result of each expression.

using System;

class Program
{
    static void Main()
    {
        // Define the mathematical expressions
        string[] expressions = {
            "-1 + 4 * 6",
            "(35 + 5) % 7",
            "14 + -4 * 6 / 11",
            "2 + 15 / 6 * 1 - 7 % 2"
        };

        // Evaluate and print each expression
        foreach (string exp in expressions)
        {
            Console.WriteLine($"Result: {EvaluateExpression(exp)}");
        }
    }

    // Function to evaluate a mathematical expression
    static int EvaluateExpression(string expression)
    {
        // Use built-in C# expression evaluation
        return (int)new System.Data.DataTable().Compute(expression, null);
    }
}


// Q2
// Pseudocode:
// 1. Read the first number from the user and store it in a variable.
// 2. Read the second number from the user and store it in another variable.
// 3. Create a temporary variable to hold one of the numbers during swapping.
// 4. Swap the values of the two variables using the temporary variable.
// 5. Print the swapped numbers.

using System;

class Program
{
    static void Main()
    {
        // Read the first number from the user
        Console.Write("Input the First Number: ");
        int firstNumber = int.Parse(Console.ReadLine());

        // Read the second number from the user
        Console.Write("Input the Second Number: ");
        int secondNumber = int.Parse(Console.ReadLine());

        // Swap the numbers
        int temp = firstNumber;
        firstNumber = secondNumber;
        secondNumber = temp;

        // Print the swapped numbers
        Console.WriteLine("After Swapping:");
        Console.WriteLine($"First Number: {firstNumber}");
        Console.WriteLine($"Second Number: {secondNumber}");
    }
}


// Q3
// Pseudocode:
// 1. Define a method named SumOrTripleSum that takes two integers, num1 and num2, as input.
// 2. Compute the sum of num1 and num2 and store it in a variable sum.
// 3. If num1 equals num2:
//      - Return triple the sum.
//    Else:
//      - Return the sum.

using System;

class Program
{
    static void Main()
    {
        // Test cases
        Console.WriteLine(SumOrTripleSum(5, 5));  // 30
        Console.WriteLine(SumOrTripleSum(5, 6));  // 11
    }

    // Method to compute the sum of two given integers, returning triple the sum if they are equal
    static int SumOrTripleSum(int num1, int num2)
    {
        int sum = num1 + num2;

        if (num1 == num2)
        {
            return 3 * sum;
        }
        else
        {
            return sum;
        }
    }
}

// Q4
// Pseudocode:
// 1. Read the temperature in Celsius from the user and store it in a variable.
// 2. Convert the temperature to Kelvin using the formula: kelvin = celsius + 273.
// 3. Convert the temperature to Fahrenheit using the formula: fahrenheit = celsius * 9 / 5 + 32.
// 4. Print the converted temperatures (Kelvin and Fahrenheit).

using System;

class Program
{
    static void Main()
    {
        // Read temperature in Celsius from the user
        Console.Write("Enter the amount of Celsius: ");
        double celsius = double.Parse(Console.ReadLine());

        // Convert Celsius to Kelvin
        double kelvin = celsius + 273;

        // Convert Celsius to Fahrenheit
        double fahrenheit = celsius * 9 / 5 + 32;

        // Print the converted temperatures
        Console.WriteLine($"Kelvin = {kelvin}");
        Console.WriteLine($"Fahrenheit = {fahrenheit}");
    }
}


// Q5
// Pseudocode:
// 1. Loop through numbers from 1 to 99.
// 2. Check if the current number is odd.
// 3. If the number is odd, print it.
// 4. Move to the next number.

using System;

class Program
{
    static void Main()
    {
        // Loop through numbers from 1 to 99
        for (int i = 1; i <= 99; i++)
        {
            // Check if the number is odd
            if (i % 2 != 0)
            {
                // Print the odd number
                Console.WriteLine(i);
            }
        }
    }
}



// Q6
// Pseudocode:
// 1. Prompt the user to press a key.
// 2. Read the pressed key.
// 3. If the pressed key is a number key (0 to 9):
//      4. Display the pressed number.
//    Else:
//      5. Display "Not allowed".

using System;

class Program
{
    static void Main()
    {
        // Step 1: Prompt the user to press a key
        Console.WriteLine("Press a key (0 to 9):");

        // Step 2: Read the pressed key
        ConsoleKeyInfo keyInfo = Console.ReadKey();

        // Step 3: If the pressed key is a number key (0 to 9)
        if (char.IsDigit(keyInfo.KeyChar))
        {
            // Step 4: Display the pressed number
            Console.WriteLine($"You pressed: {keyInfo.KeyChar}");
        }
        else
        {
            // Step 5: Display "Not allowed"
            Console.WriteLine("Not allowed");
        }
    }
}



// Q7
// Pseudocode:
// 1. Prompt the user to enter a real number.
// 2. Read the user input.
// 3. Try to parse the user input to a double.
// 4. If parsing is successful:
//      5. Calculate the square root of the number.
//      6. Display the square root.
//    Else (if parsing fails):
//      7. Display an error message.


using System;

class Program
{
    static void Main()
    {
        try
        {
            // Step 1: Prompt the user to enter a real number
            Console.Write("Enter a real number: ");
            
            // Step 2: Read the user input
            string userInput = Console.ReadLine();
            
            // Step 3: Try to parse the user input to a double
            double number = double.Parse(userInput);
            
            // Step 5: If parsing is successful, calculate the square root and display it
            double squareRoot = Math.Sqrt(number);
            Console.WriteLine($"Square root of {number} is: {squareRoot}");
        }
        catch (FormatException)
        {
            // Step 7: If parsing fails, display an error message
            Console.WriteLine("Invalid input. Please enter a valid real number.");
        }
    }
}
