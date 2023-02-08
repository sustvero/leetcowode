class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # anagrams -> hashing
        # map every word to its hash table of letters
        # compare the hash tables of each word to group them (use an outer hash table)
        # print out all values in outer hash table

        # TUPLES ARE HASHABLE
        # to turn character to ascii code, use ord() - for reverse use chr()

        
        anagrams = collections.defaultdict(list)

        for word in strs:
            letters = [0]*26
            for char in word:
                letters[ord(char) - ord('a')] += 1
            letters_combo = tuple(letters)
            if letters_combo in anagrams:
                anagrams[letters_combo].append(word)
            else:
                anagrams[letters_combo] = [word]
            
        
        # now, format the output
        return anagrams.values() 

# this solution has complexity O(n), where n is the number of characters