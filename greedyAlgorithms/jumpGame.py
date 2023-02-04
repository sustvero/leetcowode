class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # steps with 0: we must ensure we have enough steps to get through 
        # start from the last index
        # if there exists a jump to that index, see if you can make it to the previous index


        idx = len(nums) - 1
        jumpTo = len(nums) - 2 # searches for previous index where a jump to idx is possible

        while idx != 0:
            # case where jumpTo has found a possible spot we can jump to
            if jumpTo + nums[jumpTo] >= idx:
                idx = jumpTo
                jumpTo -= 1
            elif jumpTo == 0:
                return False
            else:
                jumpTo -= 1
        
        return True