class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # output array - size n
        output = [1] * len(nums)

        # we traverse the array twice
        # first time, we multiply by the product of all prefixes of each index
        # second time, we multiply by the product of all suffixes of each index

        prefix = 1

        for i in range(0, len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        
        # second traversal
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output

# this solution has time complexity O(n)