class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # base case
        if (len(nums)) == 1: return nums[0]

        # edge case: all array elements are negative
        allNegative = True
        for num in nums:
            if num > 0:
                allNegative = False
        if (allNegative):
            return max(nums)

        # keep track of the current sum and the maximum sum so far
        currentSum = 0
        maxSoFar = 0

        # iterate through array
        for num in nums:
            currentSum += num
            # if the current sum is negative, this subarray will not contribute towards creating a large sum
            if currentSum < 0:
                currentSum = 0
            if currentSum > maxSoFar: # replace the maximum so far
                maxSoFar = currentSum
        
        return maxSoFar
    
    # this algorithm has complexity O(n)