"""
Given a link list and x value, patition the link list such that all node less then list come first and large
node come next while preserving the order

                              h
1 -> 4 -> 3 -> 2 -> 5 -> 2 -> 6
                         s
                              b
slist 1, 2,2   
blist 4,3, 5 ,6
1 -> 2 -> 2 -> 4 -> 3 -> 5 -> 6

"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        slist = ListNode()
        blist = ListNode()
        s, b = slist, blist

        while head:
            if head.val > x:
                b.next = head
                b = b.next
            else:
                s.next = head
                s = s.next
            
            head = head.next

        s.next = blist
        b.next = None

        return slist.next
    