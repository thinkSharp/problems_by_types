"""
find cycle in the link list by using fast and slow pointers

    |---------------|
1 -> 2 -> 3 -> 4 -> 5 
    s
          f
                            
          s
                    f
                s
    f  
                     s
                f
    s
    f
															 
time complexity : O(n) => worst case f has to treverse 2 times to catch up the slow
space complexity = O(1)

"""
from typing import Optional
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        return False