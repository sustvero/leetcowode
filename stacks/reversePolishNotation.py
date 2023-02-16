class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # every time we come to an operational token, pop the last two numbers off the stack

        nums = []

        if (len(tokens) == 0):
            return 0
        if (len(tokens) == 1):
            return int(tokens[0])

        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                numB = nums.pop()
                numA = nums.pop()

                if token == '+':
                    nums.append(numA + numB)
                elif token == '-':
                    nums.append(numA - numB)
                elif token == '*':
                    nums.append(numA * numB)
                elif token == '/':
                    nums.append(int(numA / numB))
            
            else: # it is a number
                nums.append(int(token))

        # if the sequence is valid, there is only one resulting value in the stack
        return nums[0]
    
# this solution has complexity O(n)