# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root):
        res = []

        def dfs(node, depth):
            if not node:
                return
            if depth == len(res):        # first time reaching this level → make its bucket
                res.append([])
            res[depth].append(node.val)  # drop value into its level's bucket
            dfs(node.left, depth + 1)    # left first, so each level reads left → right
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return res