# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True   
        queue  = deque([root])
        while queue:
            node = queue.popleft()
            if self.isSameTree(node,subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
            
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p,q)])
        while queue:
            nodep, nodeq = queue.popleft()
            if not nodep and not nodeq:
                continue
            if not nodep or not nodeq:
                return False
            if nodep.val != nodeq.val:
                return False
            queue.append((nodep.left,nodeq.left))
            queue.append((nodep.right,nodeq.right))
        return True
        