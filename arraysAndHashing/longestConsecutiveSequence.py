class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use a set to keep track of which values are in the array

        # edge cases
        if len(nums) == 0:
            return 0

        elems = set(nums)

        maxLength = 1

        for elem in nums:
            if elem - 1 not in elems:
                length = 0
                while elem in elems:
                    length += 1
                    elem += 1
                if length > maxLength:
                    maxLength = length
            
        return maxLength

# time complexity: O(n)
