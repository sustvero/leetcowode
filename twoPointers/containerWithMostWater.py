class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1

        # keep track of the maximum area so far
        # always move in the direction away from the shorter stick
        # for example, if right is shorter, then move one stick left
        # stop when both left and right become equal
        # what to do when both sides are the same height?

        maxSoFar = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            if (area > maxSoFar):
                maxSoFar = area
            
            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                left += 1
                right -= 1
        
        return maxSoFar

# this solution has complexity O(n)