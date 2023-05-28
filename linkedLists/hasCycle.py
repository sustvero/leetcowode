# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # potential - change the value of the linked list to indicate it has been visited already

        # have a slow pointer (increments by 1) and a fast pointer (increments by 2)

        # edge case:
        # 0 nodes
        # 1 node

        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next

        while fast and fast.next:
            if slow == fast:
                return True
            
            slow = slow.next
            fast = fast.next.next
        
        return False
