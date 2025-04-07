using System;

class LoopsAndFunctions
{
    static void Main()
    {
        // For loop to print 1-10
        Console.WriteLine("Numbers 1 to 10:");
        for (int i = 1; i <= 10; i++)
        {
            Console.Write(i + " ");
        }
        Console.WriteLine();

        // While loop for user input
        string input = "";
        while (input.ToLower() != "exit")
        {
            Console.WriteLine("Enter a word or 'exit' to quit:");
            input = Console.ReadLine();
            Console.WriteLine($"You entered: {input}");
        }

        // Factorial function
        Console.WriteLine("Enter a number for factorial calculation:");
        int number = Convert.ToInt32(Console.ReadLine());
        long factorial = CalculateFactorial(number);
        Console.WriteLine($"Factorial of {number} is {factorial}");
    }

    static long CalculateFactorial(int n)
    {
        if (n == 0) return 1;
        long result = 1;
        for (int i = 1; i <= n; i++)
        {
            result *= i;
        }
        return result;
    }
}