class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums is already in ascending order

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
        
        if low == high and nums[low] == target:
            return low
        else:
            return -1

# this solution has O(logn) complexity