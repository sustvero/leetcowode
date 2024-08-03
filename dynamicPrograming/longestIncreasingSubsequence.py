class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # method:
        # start from the end and work backwards
        # each idx in results array is the longest sequence starting at 
        #    that index
        # need to compare current index to all previous subsequences

        res = [0] * len(nums)
        
        # base case:
        res[len(nums) - 1] = 1
        # edge case:
        if len(nums) == 1:
            return 1
        
        # iterative case
        for i in range(len(nums) - 2, -1, -1):
            for j in range(len(nums) - 1, i, -1):
                if nums[i] < nums[j]:
                    res[i] = max(1, res[i], res[j] + 1)
                else:
                    res[i] = max(1, res[i])
        
        return max(res)

        # the complexity of this is O(n^2)

        