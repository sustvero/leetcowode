class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.split()
        last_word = word_list[-1]
        
        return len(last_word)
    
# this solution has time complexity O(n)