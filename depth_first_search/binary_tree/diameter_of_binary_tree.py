"""
Diameter of a Binary Tree
 is length of the longest path (# of edges) between any two nodes

 solution approach
 - local bfs function
 - non local variable to store max diameter
 - return max length till node from bfs 
"""
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDiameter(self, root: Node) -> int:
        if root is None:
            return 0
        
        max_diameter = 0
        def dfs(node):
            nonlocal max_diameter
            if node is None:
                return 0
            
            left_length = dfs(node.left)
            right_length = dfs(node.right)

            max_diameter = max(max_diameter, left_length + right_length)
            return 1 + max(left_length, right_length)
        
        dfs(root)
        return max_diameter