class Solution:
    def isValid(self, s: str) -> bool:
        # map each closing bracket to corresponding opening bracket
        brackets_map = {"]":"[", ")":"(", "}":"{"}

        # every time we encounter a closing bracket, check the top of the stack
        b_stack = []

        for char in s:
            # 2 cases: opening bracket or closing bracket
            if char in brackets_map: # closing bracket
                if len(b_stack) and b_stack[-1] == brackets_map[char]:
                    b_stack.pop()
                else:
                    return False
            
            else:
                b_stack.append(char)
        
        # important: check that stack is empty after we've gone through entire string
        if len(b_stack) == 0:
            return True
        return False


    # this solution has complexity O(n)