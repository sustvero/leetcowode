class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # knowing the pivot point doesn't necessarily help us
        # modify binary search
        # take a look at the first and last values of each half
        # if first value < last and our target is in the range, search that half
        # if first > last we know the pivot point is contained somewhere there


        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            
            else:
                # cover all cases:
                if (nums[low] <= nums[mid]):
                    if (nums[low] <= target and nums[mid] >= target):
                        high = mid - 1
                    else:
                        low = mid + 1
                elif (nums[mid] <= nums[high]):
                    if (nums[mid] <= target and nums[high] >= target):
                        low = mid + 1
                    else:
                        high = mid - 1
        
       
        return -1

# this algorithm has runtime O(logn)