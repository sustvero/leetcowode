# solution 1: hashing
# O(n) time, O(n) space efficiency
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # use a hash table
        # keep track of frequency of each element in the list
        # once we hit the count of n / 2, we have found the majority element
        # time efficiency of this will be O(n)

        frequencies = {}
        majority = len(nums) // 2

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
            if frequencies[num] > majority:
                return num

# solution 2: Boyer-Moore algorithm
# start by taking a guess
# maintain a sum throughout
# 
