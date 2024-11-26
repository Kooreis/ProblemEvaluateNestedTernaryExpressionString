Here is a simple console application in C# that evaluates a nested ternary expression string:

```C#
using System;
using System.Collections.Generic;

public class Program
{
    public static void Main()
    {
        Console.WriteLine("Enter a ternary expression:");
        string expression = Console.ReadLine();
        Console.WriteLine("Result: " + Evaluate(expression));
    }

    public static int Evaluate(string expression)
    {
        Stack<int> stack = new Stack<int>();
        for (int i = expression.Length - 1; i >= 0; i--)
        {
            if (Char.IsDigit(expression[i]))
            {
                stack.Push(expression[i] - '0');
            }
            else if (expression[i] == '?')
            {
                int trueValue = stack.Pop();
                int falseValue = stack.Pop();
                stack.Push(expression[--i] == 'T' ? trueValue : falseValue);
            }
        }
        return stack.Peek();
    }
}
```

This program reads a ternary expression from the console, evaluates it, and prints the result. The `Evaluate` method uses a stack to keep track of the values of the sub-expressions. When it encounters a '?', it pops the top two values from the stack, and pushes the value of the ternary expression back onto the stack. The value of the ternary expression is determined by the character before the '?'. If it is 'T', the true value is used, otherwise the false value is used.