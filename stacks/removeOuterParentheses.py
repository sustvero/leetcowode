class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        # main idea: if the stack is empty, we have the outer parentheses

        stack = []
        outer = True
        res = ""

        for c in s:
            if c == "(":
                if len(stack) != 0:
                    res += c
                stack.append(c)
            else:
                stack.pop()
                if len(stack) != 0:
                    res += c
        
        return res


# time complexity is O(n)