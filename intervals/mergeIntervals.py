class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # keep track of a current interval as we loop through
        # once the next interval no longer overlaps with the current, set the next interval to be current
        # keep merging until we find a new interval that does not overlap
        intervals.sort(key=lambda pair: pair[0])

        # edge cases
        if len(intervals) == 1:
            return intervals

        current = intervals[0]
        currentIdx = 0
        res = [] # this stores the final list

        while (currentIdx < len(intervals)):
            # does not overlap
            if current[1] < intervals[currentIdx][0]:
                res.append(current)
                current = intervals[currentIdx]
            elif current[0] > intervals[currentIdx][1]:
                res.append(intervals[currentIdx])

            # overlaps
            else:
                current = [min(intervals[currentIdx][0], current[0]), max(intervals[currentIdx][1], current[1])]

            currentIdx += 1
        
        res.append(current)
        return res

        # time complexity: O(nlogn) -> sorting