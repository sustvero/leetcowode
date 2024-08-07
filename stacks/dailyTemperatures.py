class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        
        # keep a stack of pairs [temp, index]
        stack = []

        for i,t in enumerate(temperatures):
            # deduce number of days until a warmer day
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                result[index] = i - index
            stack.append([t, i])
        
        return result
    
    # time complexity of this problem is O(n)