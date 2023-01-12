

# fastest solution using hashing (dictionaries):
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check first if lengths are equal
        if len(s) != len(t):
            return False
        
        # create empty dictionaries
        # NOTE: dictionaries are basically built-in hash tables
        s_counts = {}
        t_counts = {}

        # add characters to each dictionary
        for i in range(0, len(s)):
            s_counts[s[i]] = s_counts.get(s[i], 0) + 1
            # note: get(key, value) where value is something to return if the key is not found
            t_counts[t[i]] = t_counts.get(t[i], 0) + 1
        
        # check equality of dictionaries
        return s_counts == t_counts

# this solution has runtime O(s + t)

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        # convert each string into list
        s_list = list(s)
        t_list = list(t)
        # sort each list in alphabetical order
        s_list.sort()
        t_list.sort()
        # check if lists are equal
        if (s_list == t_list):
            return True
        else:
            return False
        
# this solution has runtime O((s + t)log(s + t)