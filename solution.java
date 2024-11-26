Here is a Java console application that evaluates a nested ternary expression string:

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a ternary expression:");
        String expression = scanner.nextLine();
        System.out.println("The result is: " + parseTernary(expression));
    }

    public static int parseTernary(String expression) {
        if (expression == null || expression.length() == 0) {
            return 0;
        }
        Stack<Character> stack = new Stack<>();
        for (int i = expression.length() - 1; i >= 0; i--) {
            char c = expression.charAt(i);
            if (!stack.isEmpty() && stack.peek() == '?') {
                stack.pop(); // pop '?'
                char first = stack.pop();
                stack.pop(); // pop ':'
                char second = stack.pop();
                if (c == 'T') {
                    stack.push(first);
                } else {
                    stack.push(second);
                }
            } else {
                stack.push(c);
            }
        }
        return Character.getNumericValue(stack.peek());
    }
}
```

This console application reads a ternary expression from the user, evaluates it, and prints the result. The `parseTernary` method uses a stack to evaluate the expression from right to left. When it encounters a '?', it pops the '?' and the next two characters from the stack, which represent the two possible values of the ternary expression. It then pushes the appropriate value back onto the stack based on whether the current character is 'T' or 'F'. The final result is the numeric value of the character at the top of the stack.