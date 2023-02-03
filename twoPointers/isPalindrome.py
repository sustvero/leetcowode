class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove all non-alphanumeric characters
        # we can use isAlnum() method to check which characters are alphanumeric
        newString = ""
        for char in s:
            if char.isalnum():
                newString += char
        s = newString
        # we also need to change string to lowercase
        s = s.lower()
    
        # iterate from front of string and back of string
        i1 = 0
        i2 = len(s) - 1
        # check that all characters match
        while i1 < i2:
            if s[i1] != s[i2]:
                return False
            i1 += 1
            i2 -= 1
        
        return True


# this solution has time complexity O(n)