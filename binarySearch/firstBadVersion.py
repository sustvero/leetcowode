# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        # make use of binary search
        # always check the middle element to see if it's good or bad
        # if it's good, check right half
        # if it's bad, check if first element, then check if previous is good THEN check rest of left half

        # O(logn)

        # edge cases
        # a single bad version 
        # all versions are bad
        # a bad version is the last version created

        low = 1
        high = n

        if low == high:
            return 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if isBadVersion(mid) == False:
                # check right half
                low = mid + 1
            
            else:
                if mid == 1:
                    return 1
                elif not isBadVersion(mid - 1):
                    return mid
                else:
                    high = mid - 1
