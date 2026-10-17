# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        self.res = 0                          # best diameter found so far

        def dfs(node):                        # returns the HEIGHT of this subtree
            if not node:
                return 0
            left = dfs(node.left)             # height of left subtree
            right = dfs(node.right)           # height of right subtree
            self.res = max(self.res, left + right)   # longest path turning at this node
            return 1 + max(left, right)       # same as Max Depth: height for the parent

        dfs(root)
        return self.res
