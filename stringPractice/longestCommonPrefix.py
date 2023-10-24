class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # keep track of the current prefix 
        # maximum length of the prefix is the length of the longest word

        prefix = ""

        # precompute length of shortest word
        shortest = len(strs[0])
        for string in strs:
            if len(string) < shortest:
                shortest = len(string)
        
        for i in range(1, shortest + 1):
            prefix += strs[0][i - 1]
            for string in strs:
                if string[:i] != prefix:
                    return prefix[:-1]
        
        return prefix

        # time complexity: O(m + n) where m is the number of strings in strs
        # space complexity: O(n) where n is the number of characters in the shortest word

        # edge cases:
        # no common prefix
        # words of length 0