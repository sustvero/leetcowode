class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        res = []
        # map the counts to the values in the count
        counts = []
        for i in range(len(nums) + 1):
            counts.append([])
        frequencies = {}
        
        for elem in nums:
            if elem in frequencies:
                count = frequencies[elem]
                counts[count].remove(elem)
                counts[count + 1].append(elem)
                frequencies[elem] = count + 1
            else:
                frequencies[elem] = 1
                counts[1].append(elem)
        
        # now, we want to return the k most frequent elements
        # iterate backwards through the acounts array
        tracker = 0
        for i in range(len(nums), 0, -1):
            if len(counts[i]) > 0:
                for elem in counts[i]:
                    res.append(elem)
                    tracker += 1
                    if (tracker == k):
                        return res

# this solution has time complexity O(n)