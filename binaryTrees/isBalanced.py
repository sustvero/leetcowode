# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        # calculate depth of left subtree, depth of right subtree
        depth_left = self.depthCalculator(root.left)
        depth_right = self.depthCalculator(root.right)
        # calculate whether current tree is balanced
        return (abs(depth_left - depth_right) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def depthCalculator(self, root: Optional[TreeNode]) -> int:
        # base case
        if root == None:
            return 0
        return 1 + max(self.depthCalculator(root.left), self.depthCalculator(root.right))

# this solution has time complexity O(n^2) (?)
