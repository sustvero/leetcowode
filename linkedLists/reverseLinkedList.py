# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        # base cases
        if head == None:
            return None
        if head.next == None: # already reversed
            return head

        curnode = head.next
        head.next = None
        prev = head
        while curnode.next:
            temp = curnode.next
            curnode.next = prev
            prev = curnode
            curnode = temp  
        
        # we are now at the last node, which becomes the head
        curnode.next = prev
        head = curnode

        return head

# this solution has time complexity O(n)