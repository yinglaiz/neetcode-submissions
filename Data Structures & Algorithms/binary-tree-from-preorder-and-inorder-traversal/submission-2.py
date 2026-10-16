# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        pos = {val: i for i, val in enumerate(inorder)}   # value → index in inorder
        self.pre_i = 0                                    # pointer into preorder

        def build(left, right):            # build the tree from inorder[left..right]
            if left > right:
                return None                # empty range → no node

            val = preorder[self.pre_i]     # next pre-order value is this subtree's root
            self.pre_i += 1
            root = TreeNode(val)

            mid = pos[val]                 # O(1) lookup instead of .index()
            root.left = build(left, mid - 1)     # MUST come before right (see below)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)