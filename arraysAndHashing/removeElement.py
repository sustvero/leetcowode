class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # initialize k as length 
        # when we get to an occurrence of val:
        # decrement k by 1
        # run a loop that brings each element after val back by 1 index O(n^2)

        k = len(nums)
        idx = 0
        
        while idx < k:
            if nums[idx] != val:
                idx += 1
            else:
                k -= 1
                for j in range(idx, k):
                    nums[j] = nums[j + 1]
        return k


        