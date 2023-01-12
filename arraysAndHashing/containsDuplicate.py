class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #create an empty set
        hashset = set()
        # for each element in nums, check if it is already in the set
        for elem in nums:
            if elem in hashset:
                return True
            else:
                hashset.add(elem)
        return False
        
# this solution has runtime O(n)

class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #sort nums
        nums.sort()
        #iterate through nums, find whether any element has a duplicate
        nums_len = len(nums)
        for i in range(0, nums_len):
            if (i > 0 and nums[i] == nums[i - 1]):
                return True
        return False


# this solution has runtime O(nlogn)

