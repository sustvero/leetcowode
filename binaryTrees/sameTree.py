# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # base case:
        if p == None or q == None: 
            if q == None and p == None:
                return True
            else: 
                return False # structures do not match up

        # check whether node values are the same
        if p.val != q.val:
            return False
        else:
            return True and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
