# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(root, L):
            if root:
                if not root.left and not root.right:
                    L.append(root.val)
                if root.left:
                    dfs(root.left, L)
                if root.right:
                    dfs(root.right, L)
        
        r1, r2 = [], []
        
        dfs(root1, r1)
        dfs(root2, r2)
        
        return r1 == r2
