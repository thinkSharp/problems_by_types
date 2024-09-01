"""
level order sum of the binary tree
we can BFS to perform the sum at each level
starting with root,
add sum of root and get all it's children to queue
then process that level, sum and append children
until we reach the leaf nodes


"""
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

class Solution:
    def level_sum(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        result = []
        queue = deque([root])

        while queue:
            length = len(queue)
            curr_sum = 0
            for _ in range(length):
                node = queue.popleft()
                curr_sum += node.value

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(curr_sum)


        return result
    
