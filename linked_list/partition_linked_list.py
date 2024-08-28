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
        big_list = ListNode()
        small_list = ListNode()
        big, small = big_list, small_list
        while head:
            if head.val >= x:
                big.next = head
                big = big.next
            else:
                small.next = head
                small = small.next
            head = head.next

        small.next = big_list.next
        big.next = None

        return small_list.next
    