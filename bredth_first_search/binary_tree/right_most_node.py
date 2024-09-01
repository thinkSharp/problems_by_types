"""
Return the right most node at each level of the binary tree
using BFS we can treverse the tree and get the right most node

"""
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightMost(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.pop()
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
    