from collections import deque   # deque = double-ended queue; fast (O(1)) add/remove at both ends

class Solution:
    # Optional[TreeNode] = type hint: "either a TreeNode or None". Just documentation, Python doesn't enforce it.
    # root = the top node of the tree (node 1). It never moves in this BFS version.
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:                  # empty tree (root is None) → nothing to invert
            return None

        queue = deque([root])         # queue starts holding just the root node OBJECT (not the number 1)

        while queue:                  # keeps looping while queue is non-empty (empty deque counts as False)
            node = queue.popleft()    # remove the front node and point `node` at it (no copy made)
                                      # `node` = the node currently being processed; name could be anything (curr, n...)

            node.left, node.right = node.right, node.left
                                      # swap in one line, no temp variable needed
                                      # this MUTATES the real node, so the actual tree changes

            # Swapping only fixed this node's direct children.
            # Their children (grandchildren) still need swapping, so queue them up.
            # Order they're processed in doesn't matter: every node just needs visiting once.
            if node.left:             # skip None children (leaves have none)
                queue.append(node.left)    # add to the BACK → whole level finishes before the next (BFS)
            if node.right:
                queue.append(node.right)

        return root                   # root still points at node 1, now the top of the inverted tree