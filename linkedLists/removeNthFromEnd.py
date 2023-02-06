# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # first pass to find out total count of nodes?
        curnode = head
        count = 0
        while (curnode):
            count += 1
            curnode = curnode.next

        # edge case: n is greater than count
        if n > count:
            return head

        # edge case: only one node in 
        if not head.next:
            return None

        # edge case: removing the first node
        if n == count:
            head = head.next
            return head

        # we remove the node during the second pass
        curnode = head
        # find the correct location
        for i in range(0, count - n - 1):
            curnode = curnode.next
        # remove the node
        remove = curnode.next
        if (remove.next):
            temp = remove.next
            curnode.next = temp # skip over the node being removed
        else: # we are removing the last node
            curnode.next = None

        return head
    
    # this solution has time complexity O(n)