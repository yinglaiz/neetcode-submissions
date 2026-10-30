"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew = {}

        def dfs(node):
            if node in oldtonew:
                return oldtonew[node]

            copy = Node(node.val)     #creates a Deep copy of node called copy
            oldtonew[node] = copy   #add the deep copy called copy to the library

            for neighs in node.neighbors:
                copy.neighbors.append(dfs(neighs))
            
            return copy

        return dfs(node) if node else None 