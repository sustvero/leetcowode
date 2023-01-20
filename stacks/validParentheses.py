class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        #iterate through string
        for i in range(0, len(s)):
            # get top of stack (or 0 if no stack exists)
            if len(stack) > 0:
                stack_top = stack[len(stack) - 1]
            else:
                stack_top = '0'
            # push onto stack
            if s[i] == '[' or s[i] == '(' or s[i] == '{':
                stack.append(s[i])
            # pop from stack
            elif (s[i] == ']' and stack_top == '[') or (s[i] == ')' and stack_top == '(') or (s[i] == '}' and stack_top == '{'):
                # pop from stack
                stack.pop(len(stack) - 1)
            else:
                # invalid bracket
                return False

        return len(stack) == 0

    # this solution has complexity O(n)