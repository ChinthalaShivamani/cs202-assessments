using System;

class CalculatorWithExceptions
{
    static void Main()
    {
        try
        {
            Console.WriteLine("Enter first number:");
            double num1 = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Enter second number:");
            double num2 = Convert.ToDouble(Console.ReadLine());

            double sum = num1 + num2;
            double difference = num1 - num2;
            double product = num1 * num2;

            Console.WriteLine($"Sum: {sum}");
            Console.WriteLine($"Difference: {difference}");
            Console.WriteLine($"Product: {product}");

            // Division with exception handling
            try
            {
                double quotient = num1 / num2;
                Console.WriteLine($"Quotient: {quotient}");
            }
            catch (DivideByZeroException)
            {
                Console.WriteLine("Error: Division by zero is not allowed");
            }

            // Check if sum is even or odd
            Console.WriteLine(sum % 2 == 0 ? "The sum is even" : "The sum is odd");
        }
        catch (FormatException)
        {
            Console.WriteLine("Error: Please enter valid numbers");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An unexpected error occurred: {ex.Message}");
        }
        finally
        {
            Console.WriteLine("Calculation completed");
        }
    }
}