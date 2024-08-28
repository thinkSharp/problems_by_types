"""
Reorder the list from 
L0 , L1, ...., Ln
L0, Ln, L1, Ln-1, ....

idea is to use slow and fast pointer to get to the middle of the list
then reverse the list from the middle to the end

1 -> 2 -> 3 <- 4 <- 5
                    s
                        f
f
                    l
reverse logic:
prev = None
while slow:
temp = slow.next
slow.next = prev
prev = slow
slow = temp

dummy = ListNode()
d = dummy
while last:
 d.next = first
 d = first
 first = first.next
 d.next = last
 last = last.next

 return d.next

Time complexity is O(n)
space complexity is O(1)
"""
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        1 -> 2 -> 3 <- 4 <- 5
                            f
                            s
                            p
                            t
        f
                            l
        d
        """
        if not head:
            return None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #reverse the second half
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        first, last = head, prev
        while last.next:
            first.next, first = last, first.next
            last.next, last = first, last.next
            
        return None
    