using System;

class Calculator
{
    static void Main()
    {
        Console.WriteLine("Enter first number:");
        double num1 = Convert.ToDouble(Console.ReadLine());
        
        Console.WriteLine("Enter second number:");
        double num2 = Convert.ToDouble(Console.ReadLine());

        // Arithmetic operations
        double sum = num1 + num2;
        double difference = num1 - num2;
        double product = num1 * num2;
        
        Console.WriteLine($"Sum: {sum}");
        Console.WriteLine($"Difference: {difference}");
        Console.WriteLine($"Product: {product}");

        // Division with error handling
        if (num2 != 0)
        {
            double quotient = num1 / num2;
            Console.WriteLine($"Quotient: {quotient}");
        }
        else
        {
            Console.WriteLine("Cannot divide by zero");
        }

        // Check if sum is even or odd
        if (sum % 2 == 0)
        {
            Console.WriteLine("The sum is even");
        }
        else
        {
            Console.WriteLine("The sum is odd");
        }
    }
}