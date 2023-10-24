class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # dp solution
        # find max count for each length of subarray ending at index i
        subarrays = [0] * len(nums)

        # base case: 
        subarrays[0] = nums[0]

        # for each element, choose between current subarray or new element only
        for i in range(1, len(nums)):
            subarrays[i] = max(subarrays[i - 1] + nums[i], nums[i])
        
        return max(subarrays)
    
    # runs in O(n) time