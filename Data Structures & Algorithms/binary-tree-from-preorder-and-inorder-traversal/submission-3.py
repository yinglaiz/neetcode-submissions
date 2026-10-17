# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #1. build a dict for the inorder list
        inord = {val : i for i, val in enumerate(inorder)}
        self.pre_ind = 0

        #build subtree builder taking index
        def subtree(left, right):
            if left > right:
                return None

            val = preorder[self.pre_ind]
            self.pre_ind += 1
            root = TreeNode(val)

            mid  = inord[val] 
            root.left  = subtree(left ,mid -1)
            root.right = subtree(mid + 1, right)
            return root
        return subtree(0, len(preorder)-1)