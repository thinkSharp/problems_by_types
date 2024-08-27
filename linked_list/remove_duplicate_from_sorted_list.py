"""
Remove duplicate elements from sorted list
ex:
                                        h
1 -> 2 -> 3 -> 3 -> 3 -> 4 -> 4 -> 5 -> 6
                                    p - - - - - - - - - - - -          |
p = newnode(0, h)
a = p
1,2,5
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicate(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(0, head)
        ans = prev
        while head and head.next:
            if head.val == head.next.val:
                while head.next  and head.val == head.next.val:
                    head.next = head.next.next
                prev.next = head.next
            else:
                prev = prev.next

            head = head.next

        return ans.next
        
