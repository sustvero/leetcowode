class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numbers = {}

        # iterate through nums
        # for each number, check if target - number is contained in the numbers dictionary
        # if so, return indices
        # if not, add number to dictionary (map to index)

        for i in range(0, len(nums)): # CAREFUL: FOR LOOPS AUTOMATICALLY STOP AT END INDEX - 1
            print(target - nums[i])
            if (target - nums[i]) in numbers:
                return[(numbers[target - nums[i]]), i]
            else:
                numbers[nums[i]] = i

# this solution has time complexity O(n)