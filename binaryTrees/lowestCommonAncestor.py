# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # make a list of ancestors of each node?
        # from the end, start removing nodes until we find a common ancestor
        p_anc = self.getAncestors(root, p)
        q_anc = self.getAncestors(root, q)

        i = 0
        while i < len(p_anc) and i < len(q_anc) and p_anc[i] == q_anc[i]:
            i += 1
        
        return p_anc[i - 1]

    # helper function that returns a list of each node's ancestors
    def getAncestors(self, root: 'TreeNode', p: 'TreeNode') -> List['TreeNode']:
        ancestors = []
        curnode = root

        while p.val != curnode.val:
            ancestors.append(curnode)
            if p.val > curnode.val:
                curnode = curnode.right
            else:
                curnode = curnode.left
        
        ancestors.append(curnode) # current node
        return ancestors

    # this solution is O(logn)
