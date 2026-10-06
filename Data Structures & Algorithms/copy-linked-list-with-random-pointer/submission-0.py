"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtocopy = {None: None}
        point = head
        while point:
            oldtocopy[point] = Node(point.val)
            point = point.next

        point = head
        while point:
            copy = oldtocopy[point]
            copy.next = oldtocopy[point.next]
            copy.random = oldtocopy[point.random]
            point = point.next
        return oldtocopy[head]