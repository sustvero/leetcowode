# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        elif not root.left and not root.right:
            return [[root.val]]
        # recursion might be useful here

        orderList = []
        # we always add left subtree first, then right subtree

        def buildList(root: Optional[TreeNode], index: int):
            if not root:
                return
            if len(orderList) <= index:
                orderList.append([])
            orderList[index].append(root.val)
            buildList(root.left, index + 1)
            buildList(root.right, index + 1)
        
        # run recursive buildList function
        buildList(root, 0)
        return orderList

 # this solution has time complexity O(n)

