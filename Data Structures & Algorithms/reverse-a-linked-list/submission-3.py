# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head       #head = ListNode(val=0, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=None))))
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        return prev