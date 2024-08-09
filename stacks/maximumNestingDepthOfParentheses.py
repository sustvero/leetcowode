class Solution:
    def maxDepth(self, s: str) -> int:
        
        # ignore everything else except opening and closing parentheses
        # length of stack will indiate current depth of parentheses

        stack = []
        max_nesting_depth = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
                if len(stack) > max_nesting_depth:
                    max_nesting_depth += 1
            elif s[i] == ")":
                stack.pop()
        
        return max_nesting_depth

# time complexity: O(n)