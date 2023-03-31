class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert number to string
        # check if the string is a palindrome

        x_str = str(x)

        first = 0
        last = len(x_str) - 1

        while first < last:
            if x_str[first] != x_str[last]:
                return False
            else: 
                first += 1
                last -= 1
        
        return True

# this solution has time complexity O(n), where n is the number of digits in x