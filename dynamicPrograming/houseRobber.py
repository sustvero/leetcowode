class Solution:
    def rob(self, nums: List[int]) -> int:

        # create results array
        res = [0] * len(nums)

        if len(nums) == 0:
            return 0

        if (len(nums)) == 1:
            return nums[0]

        # base cases:
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])


        # recursive case: 
        # what is the choice we are making?
        # rob this house and skip the previous, or skip this house

        for i in range(2, len(nums)):
            res[i] = max(res[i - 2] + nums[i], res[i - 1])
        
        # return the result
        return res[len(nums) - 1]

# this solution has complexity O(n)