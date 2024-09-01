"""
given binary tree return zigzag level order traversal
using Bredth first search we can perform this
get all level order elements
append to the result either as it is or reverse order depending on the level
use mod to calculate this
keep track of level variable as well
"""
from collections import deque
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        level = 0
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            if level % 2 == 0:
                result.append(current_level)
            else:
                result.append(current_level[::-1])
            
            level += 1

        return result
    
            