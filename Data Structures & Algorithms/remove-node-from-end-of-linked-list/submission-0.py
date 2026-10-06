# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        count = 1
        while fast.next:
            fast = fast.next
            count += 1
        
        if n == count:
            return head.next
        
        frontcount = count - n -1
        slow = head
        while frontcount > 0:
            slow = slow.next
            frontcount -= 1
        slow.next = slow.next.next
        return head
        