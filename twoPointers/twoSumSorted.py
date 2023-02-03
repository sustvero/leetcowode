class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # output array
        result = []

        # have one pointer to start of array and one pointer to end of array
        i1 = 0
        i2 = len(numbers) - 1

        while i1 < i2:
            num1 = numbers[i1]
            num2 = numbers[i2]
            if num1 + num2 < target:
                # increase num1
                i1 += 1
            elif num1 + num2 > target:
                # decrease num2
                i2 -= 1
            else: # found target sum
                result.append(i1 + 1) # index is given between 1 and numbers length
                result.append(i2 + 1)
                break
        
        return result

# this solution has time complexity O(n)