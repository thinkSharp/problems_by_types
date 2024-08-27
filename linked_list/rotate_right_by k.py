"""
Rotate Right by K

1, 2, 3, 4, 5 if k = 2
5,1,2,3,4
4,5,1,2,3
position = k % length = 2 % 5 = 2
current count = length - position - 1 = 5 - 2- 1

if k = 4
5,1,2,3,4
4,5,1,2,3
3,4,5,1,2
2,3,4,5,1
last: k % length = 4 % 5 = 1
if k 8
5,1,2,3,4
4,5,1,2,3
3,4,5,1,2
2,3,4,5,1
1,2,3,4,5
5,1,2,3,4
4,5,1,2,3
3,4,5,1,2
last: k % length = 8 % 5 = 
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, )