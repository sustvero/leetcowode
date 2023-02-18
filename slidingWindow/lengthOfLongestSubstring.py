class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxLength = 0
        curString = ""

        for i in range(0, len(s)):

            if s[i] in curString:
                # remove characters from front of curstring until we can proceed
                while s[i] in curString:
                    curString = curString[1::] # remove character from front
                curString += s[i]
 
            else:
                # add to curString
                curString += s[i]
                # check against maxLength
                if len(curString) > maxLength:
                    maxLength = len(curString)
                

        return maxLength

# this solution has complexity O(n)