class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        # create a hashmap of the characters in s

        # iterate through each character in s to see how many pairs of characters we have in the hashmap
        # update hashmap to remove pairs
        # check if hashmap is empty? if it isn't, add 1 to the total of pairs

        # O(n)

        # edge cases:
        # s only contains a single letter
        # differentiate between odd length palindrome and even length palindrome
        # only palindrome of length 1 can be created

        hashmap = {}

        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
        
        pairs = 0
        single_letter = 0
        for char in s:
            if hashmap[char] > 1:
                hashmap[char] -= 2
                pairs += 1
            
            if hashmap[char] == 1:
                single_letter = 1
        
        return (pairs * 2) + single_letter