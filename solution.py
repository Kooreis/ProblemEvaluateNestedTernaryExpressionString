first = stack.pop()
                stack.pop() # pop ':'
                second = stack.pop()
                if c == 'T':
                    stack.append(first)
                else:
                    stack.append(second)