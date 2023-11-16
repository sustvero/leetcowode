# Definition for singly-linked list.
class Node:
     def __init__(self, val=0, next=None):
         self.val = val
         self.children = next
         self.end = False

class Trie:
    # map letter to corresponding node
    # prefixes start in children of trie root

    def __init__(self):
        self.root = Node("", None)

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            # check if current letter is within children of current node
            # if not, create new children
            letters = curr.children
            if curr.children == None:
                # create new children dictionary
                letters = {}
            # create new child
            if word[i] not in letters:
                letters[word[i]] = Node(word[i], None)
            curr.children = letters
            # update current
            curr = curr.children[word[i]]
        curr.end = True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            # check if child exists
            if curr.children == None or not prefix[i] in curr.children:
                return False
            else:
                curr = curr.children[prefix[i]]
        return True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            # check if child exists
            if curr.children == None or not word[i] in curr.children:
                return False
            else:
                curr = curr.children[word[i]]
        if curr.end == True:
            return True
        return False
            

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)