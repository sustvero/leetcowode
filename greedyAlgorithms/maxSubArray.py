class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # keep track of the maximum array so far
        # restart the maxSoFar array when array becomes negative (it can't possibly be added to the max array)

        maxSoFar = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):
            if maxSoFar < 0:
                maxSoFar = 0
            maxSoFar += nums[i]
            maxSum = max(maxSum, maxSoFar)
            
        return maxSum

# this solution has time complexity O(n)