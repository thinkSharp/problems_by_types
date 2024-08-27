"""
there are k sorted linked list. Merge them all
intuitation:
[[1,2],[3,4],[3,6],[2,4]]
[[1,2,3,4],[2,3,4,6]]
[[1,2,3,4,6]]
time complexity O(nlogk)
"""
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergkLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(list) == 0:
            return None
        while len(lists) > 1:
            temp = []
            for i in range(len(lists), 2):
                l1 = lists[i]
                l2 = list[i + 1] if i + 1 <= len(lists) - 1 else None
                temp.append(self.merge_lists(l1, l2))
            lists = temp
        return list[0]
    
    def merge_lists(self, l1: ListNode, l2:Optional[ListNode]) -> ListNode:
        node = ListNode()
        ans = node

        while l1 and l2:
            if l1.val > l2.val:
                node.next =l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node = node.next
        
        if l1:
            node.next = l1
        
        if l2:
            node.next = l2

        return ans.next
    