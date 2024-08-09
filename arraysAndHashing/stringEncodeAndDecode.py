class Solution:

    def encode(self, strs: List[str]) -> str:
        
        # we encode the string by putting the number of chars
        # then a character that denotes the end of the number
        # then the string

        res = ""
        for word in strs:
            res += str(len(word)) + "*" + word
        return res
            

    def decode(self, s: str) -> List[str]:

        res = []
        # nested while loop
        i = 0
        while i < len(s):
            # get index of next *
            j = i
            while s[j] != '*':
                j += 1
            num_chars = int(s[i:j])
            word = ""
            for k in range(j + 1, j + 1 + num_chars):
                word += s[k]
                
            res.append(word)
            i = j + 1 + num_chars
        
        return res

# time complexity: O(m) where m is number of characters
            

        
