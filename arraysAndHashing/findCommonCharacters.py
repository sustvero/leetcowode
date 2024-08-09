class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        # hash table: fixed array of size 26
        current_char_counts = [0] * 26
        common_char_counts = [0] * 26

        # initialize common_char_counts using first word
        for char in words[0]:
            common_char_counts[ord(char) - ord('a')] += 1

        # iterate through the rest of the words
        for i in range(1, len(words)):
            current_char_counts = [0] * 26
            # note current character counts
            for char in words[i]:
                current_char_counts[ord(char) - ord('a')] += 1
            # compare to common char counts
            for j in range(26):
                common_char_counts[j] = min(common_char_counts[j], current_char_counts[j])
        
        # form return array
        res = []
        for i in range(26):
            for j in range(common_char_counts[i]):
                res.append(chr(i + ord('a')))
        
        return res

# time complexity: O(n) where n is total number of characters