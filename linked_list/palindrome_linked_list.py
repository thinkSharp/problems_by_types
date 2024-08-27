"""
Palindrome Linked list are same front to back
ex: 1-> 2 ->2 -> 1
        s
            f
use slow and fast link list
"""
from typing import Optional
class ListNode:
    def __inti__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrom(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        node = None
        while slow:
            temp = slow.next
            slow.next = node
            node = slow
            slow = temp
        
        first = head
        second = node

        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True
    