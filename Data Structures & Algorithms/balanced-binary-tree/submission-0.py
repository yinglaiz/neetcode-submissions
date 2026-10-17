# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root):
        self.balanced = True                  # assume balanced until proven otherwise

        def subbal(node):                     # returns the HEIGHT of this subtree
            if not node:
                return 0
            left = subbal(node.left)
            right = subbal(node.right)
            if abs(left - right) > 1:         # abs() = absolute value, ignores the sign
                self.balanced = False
            return 1 + max(left, right)

        subbal(root)
        return self.balanced
            