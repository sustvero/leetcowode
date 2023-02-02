class Solution:
    def climbStairs(self, n: int) -> int:
        # initialize results array
        results = [0] * n
        # each value in results holds the number of ways to climb to the top for that number of steps
        # base cases
        if n == 0: return 0
        if n == 1: return 1
        results[0] = 1 
        # only 1 step needed to climb to the top
        results[1] = 2
        # either take 2 steps individually, or climb 2 steps at once

        # recurrence relation
        for i in range(2, n):
            results[i] = (results[i - 1]) + (results[i - 2])
        
        return results[n - 1]

# this solution has time complexity O(n)