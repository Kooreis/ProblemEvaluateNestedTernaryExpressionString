Here is a Python console application that evaluates a nested ternary expression string:

```python
class Solution:
    def parseTernary(self, expression):
        if expression is None or len(expression) == 0:
            return ""
        stack = []
        for i in range(len(expression) - 1, -1, -1):
            c = expression[i]
            if len(stack) != 0 and stack[-1] == '?':
                stack.pop() # pop '?'
                first = stack.pop()
                stack.pop() # pop ':'
                second = stack.pop()
                if c == 'T':
                    stack.append(first)
                else:
                    stack.append(second)
            else:
                stack.append(c)
        return str(stack[0])

if __name__ == "__main__":
    s = Solution()
    expression = input("Enter a ternary expression: ")
    print("The result is: ", s.parseTernary(expression))
```

This console application takes a ternary expression as input and outputs the result of the expression. The ternary expression should be in the format of "T?X:Y", where T is a boolean value (T for true, F for false), X is the value if T is true, and Y is the value if T is false. The ternary expression can be nested, for example, "T?T?1:2:F?3:4".