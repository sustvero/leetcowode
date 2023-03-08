class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search will help us here
        # since the array is sorted, we know that the minimum value will be right after the maximum value
        # modify binary search to find whether values are increasing or decreasing
        # check the next value

        # edge case: rotated by zero (or a full rotation)
        # this will be the only case where the first element of the list is less than the last element
        if nums[0] < nums[len(nums) - 1]: 
            return nums[0]

        # another edge case - only one element
        if len(nums) == 1:
            return nums[0]
        
        # modified binary search
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1] # we have found the min
            elif nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[mid] > nums[len(nums) - 1]:
                low = mid + 1 # right half
            else:
                high = mid - 1 # left half
        
        return nums[0]
        
        # runtime: O(n)