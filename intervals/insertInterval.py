class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # edge cases:
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals

        res = []

        for i in range(0, len(intervals)):
            if newInterval[1] < intervals[i][0]: # no overlap
                res.append(newInterval)
                res += intervals[i::]
                return res
            elif newInterval[0] > intervals[i][1]: # no overlap
                res.append(intervals[i])
            else: # overlap
                newStart = min(newInterval[0], intervals[i][0])
                newEnd = max(newInterval[1], intervals[i][1])
                newInterval = [newStart, newEnd]
        
        res.append(newInterval) # case if newInterval is greatest interval left
        return res

# this solution has time complexity O(n)