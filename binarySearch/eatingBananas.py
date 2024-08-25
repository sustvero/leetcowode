import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        min_speed = r

        while l <= r:
            k = (l + r) // 2

            count = 0

            for pile in piles:
                count += math.ceil(float(pile / k))
            
            if count > h:
                l = k + 1
            else:
                min_speed = k
                r = k - 1
            
        return min_speed