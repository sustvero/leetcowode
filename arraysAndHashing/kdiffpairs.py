class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        # turn nums into a set 
        pairset = set()
        frequencies = {}

        for elem in nums:
            frequencies[elem] = frequencies.get(elem, 0) + 1

        for elem in nums:
            if (elem - k) in frequencies:
                if k == 0 and frequencies[elem] > 1: # edge case -> k = 0
                    pairset.add((elem, elem))
                elif k != 0:
                    pairset.add((elem, elem - k))
                # set does not allow for duplicate elements
            
        return len(pairset)


        

        # this solution has time complexity O(n)