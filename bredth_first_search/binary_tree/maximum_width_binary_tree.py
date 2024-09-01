"""
find the max width of the binary tree:
solution approach:
using BFS do level treverse
at each level, we can calculate position no from parent position:
if parent position 0 => left 2 * 0 , right 2 * 0 + 1
if parent position 3 => left 2 * 3, right 2 * 3 + 1
when we add node in the queu, add position along wih it
"""
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maximumWidthBTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_width = 1
        queue = deque([root, 0])

        while queue:

            level_size = len(queue)
            first_pos, last_pos = queue[0][1], -1

            for i in range(level_size):
                node, pos = queue.popleft()

                if i == level_size - 1:
                    last_pos = pos 

                if node.left:
                    queue.append([node.left, pos * 2])
                
                if node.right:
                    queue.append([node.right, pos * 2 + 1])

            if first_pos != -1 and last_pos != -1:
                max_width = max(max_width, last_pos - first_pos + 1)

        return max_width

