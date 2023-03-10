# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # indicate that we have visited the node already by changing its value
        # given nodes will only have values up to 10 ** 5
        # so to indicate we've visited the node, we set its value to 10 ** 5 + 1

        curnode = head
        while curnode:
            if curnode.val == (10 ** 5) + 1:
                return True
            curnode.val = (10 ** 5) + 1
            curnode = curnode.next
        
        return False

# this solution has time complexity O(n)