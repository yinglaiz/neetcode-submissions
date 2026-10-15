# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxval):              #don;t need a self as it is plain function and not method of solution
            if not node:
                return 0
            
            goodval = 1 if node.val >= maxval else 0
            maxval  = max(maxval, node.val)
            return goodval +dfs(node.left, maxval) + dfs(node.right, maxval)

        return dfs(root, root.val)