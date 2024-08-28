"""
Remove nth node solving two ways

1). loop through the end to get the count
    get the stop count length - n + 1
    have dummy pointer to support edge case
    have current pointer point to dummy loop till stop count
    adjust the pointers

2). Single pass
    create dummy variable
    left = right = dummy
    loop right till n + 1
    then continue loop right till end
    this time move left along
    when right points to None
    left.next = left.next.next

"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        count, curr = 0, head
        while curr:
            count += 1
            curr = curr.next
        
        stop_count, count = count - n + 1, 0
        curr = dummy
        while curr:
            count += 1
            if count == stop_count:
                curr.next = curr.next.next
            curr = curr.next
        return dummy.next
    
    def removeNthFromEnd_one_pass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        left = right = dummy
        for _ in range(n + 1):
            right = right.next
        
        while right:
            left, right = left.next, right.next
        
        left.next = left.next.next

        return dummy.next
    

