# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # edge cases - lists are empty
        if (list1 == None):
            return list2
        elif (list2 == None):
            return list1
        
        # iterate through list1
        # if the next node in list2 <= next node in list1, insert that node into list
        curhead = None
        curnode1 = None
        curnode2 = None
        
        new_head = ListNode() # blank listnode
        new_curnode = new_head

        while list1 and list2:
            if list1.val < list2.val:
                new_curnode.next = list1
                list1 = list1.next
            else:
                new_curnode.next = list2
                list2 = list2.next
            new_curnode = new_curnode.next
        
        if (list1):
            new_curnode.next = list1 # remainder of list1
        elif (list2):
            new_curnode.next = list2 # remainder of list2
        
        return new_head.next



    # total runtime: O(n) where n is the sum of nodes in list1 and list2
