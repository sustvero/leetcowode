# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry_on = 0

        result = ListNode(0, None)
        res_head = result

        curr1 = l1
        curr2 = l2

        while (curr1 or curr2):
            val1 = 0
            val2 = 0
            if (curr1):
                val1 = curr1.val
                curr1 = curr1.next
            if (curr2):
                val2 = curr2.val
                curr2 = curr2.next
            sum_val = val1 + val2 + carry_on
            result.next = ListNode(sum_val % 10, None)
            result = result.next
            carry_on = sum_val // 10
        
        if (carry_on) > 0:
            result.next = ListNode(carry_on, None)
        
        # finally, reverse the result
        return res_head.next

# this solution has time complexity O(n)