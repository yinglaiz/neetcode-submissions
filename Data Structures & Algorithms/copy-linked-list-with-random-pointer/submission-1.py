"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next        # arrow to the next box
        self.random = random    # extra arrow: can point at ANY box, or None
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Example used in comments: [7] → [13] → [11] → None
        #   7.random → None, 13.random → 7, 11.random → 13

        # Lookup table: original box → its copy box
        # {None: None} so that looking up None (end of list / empty random) gives None
        oldtocopy = {None: None}

        # ---------- Pass 1: create a copy box for every original box ----------
        point = head                                # finger on the first original box
        while point:                                # until we fall off the end
            oldtocopy[point] = Node(point.val)      # key: original box, value: new box with same number
                                                    # (no arrows yet: next and random are None)
            point = point.next                      # move to the next original box
        # oldtocopy: {None: None, [7]: [7'], [13]: [13'], [11]: [11']}
        # copies exist but are loose: [7']  [13']  [11']

        # ---------- Pass 2: copy the arrows onto the copy boxes ----------
        point = head                                # finger back on the first original box
        while point:
            copy = oldtocopy[point]                 # finger on this box's copy (e.g. [7'])
            copy.next = oldtocopy[point.next]       # original's next is [13] → translate to [13'] → 7' → 13'
            copy.random = oldtocopy[point.random]   # original's random → translate to its copy
            point = point.next                      # move to the next original box
        # Result: [7'] → [13'] → [11'] → None, 13'.random → 7', 11'.random → 13'

        return oldtocopy[head]                      # copy of the first box = head of the new list



        ###Key understanding
'''
1. Variables are fingers, nodes are boxes.
point, copy, head are fingers. Writing a variable's name always means "the box it's pointing at right now". That includes inside a dictionary's [], so oldtocopy[point] uses the box as the key, not the finger. Moving the finger later doesn't change what's already stored.

2. The dictionary is a lookup table, not a linked list.
Both the keys and the values are boxes: original box → copy box. It holds no arrows and no order. It only answers "what's the copy of this box?"

3. Each part does one job:

Node(point.val) creates a copy box (same number, no arrows yet)
the original list (via point.next, point.random) knows where the arrows go
the dict translates that target into its copy
copy is the finger on the box whose arrows you're drawing

4. Why two passes: a random arrow can point at a box further ahead. If you copied and wired in one pass, that box's copy might not exist yet. Creating every copy first means every lookup in pass 2 succeeds.
'''