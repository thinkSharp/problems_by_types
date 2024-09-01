"""
given binary tree generate the level-order traversal of the tree
using Bredth
"""
from collections import deque
class TreeNode:
    def __init_(self, val=0, left=None, right=None):
        self.value= val
        self.left=left
        self.right=right

class Solution:
    def level_order(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        result = []
        queue = deque([root])

        while queue:

            size = len(queue)
            current_level = []

            while _ in range(size):
                node = queue.popleft()
                current_level.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.extend(current_level)
        return result
    
        