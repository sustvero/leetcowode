class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # hash table implementation?
        # seems kind of like two sum
        # note that pairs should be distinct
        # create a set, then check for pairs?

        pairs = 0
        

        # have hash table for %60
        times = [0] * 60
        for t in time:
            times[t % 60] += 1
        
        for i in range(1, 30):
            pairs += times[i] * times[60 - i]
        
        # special cases: 0 and 30
        # number of pairs formula: n(n - 1) / 2
        pairs += ((times[0]) * (times[0] - 1)) / 2
        pairs += ((times[30]) * (times[30] - 1)) / 2

        return int(pairs)

        # time complexity: O(n)

        