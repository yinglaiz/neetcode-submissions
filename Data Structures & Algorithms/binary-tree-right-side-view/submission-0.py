# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                place = queue.popleft()
                if place.left:
                    queue.append(place.left)
                if place.right:
                    queue.append(place.right)
            res.append(place.val)
        return res

