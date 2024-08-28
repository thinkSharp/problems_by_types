"""
In order to swap pairs,
we will use three pointers and dummy
dummy
d = dummy
prev, curr, = head, head.next
prev.next, curr.next = curr.next, prev
d.next, d = curr, prev
prev = prev.next
curr = prev.next if prev else None

2 -> 1 -> 3 -> 4
               p
                       c
				                      t
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode()
        d = dummy
        prev, curr = head, head.next

        while curr:
            prev.next, curr.next = curr.next, prev
            d.next, d = curr, prev
            prev = prev.next
            curr = prev.next if prev else None

        return dummy.next