class Solution:
    def parseTernary(self, expression):
        if expression is None or len(expression) == 0:
            return ""
        stack = []
        for i in range(len(expression) - 1, -1, -1):
            c = expression[i]
            if len(stack) != 0 and stack[-1] == '?':
                stack.pop() # pop '?'