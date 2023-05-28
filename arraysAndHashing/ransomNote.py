class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # set of letters in ransomNote needs to be subset of magazine

        # sort both strings, then compare them letter by letter
        # convert ransomNote and magazine into sets using built-in set() function
        # then check if ransomNote is subset of magazine 
        # THIS DOES NOT WORK! sets only contain unique values

        # new strategy: use a hash map
        # create a hash map from magazine letters
        # for each letter in ransomNote, check if it's contained in the hash map
        # if it is, update hash map not to include that letter anymore

        # O(n + m) where n is the number of characters in ransomNote, m the number of characters in magazine

        mag_map = {}

        for char in magazine:
            mag_map[char] = mag_map.get(char, 0) + 1
        
        for letter in ransomNote:
            if letter not in mag_map or mag_map[letter] < 1:
                return False
            else:
                mag_map[letter] -= 1
        
        return True
        