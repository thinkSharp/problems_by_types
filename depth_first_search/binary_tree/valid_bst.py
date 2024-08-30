"""
Valid binary search tree is a good tree, if left side and less then root.val and right side is greather then root.val
and left sub tree is valid tree and right sub tree is valid tree
"""
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def validBTS(self, root: Node) -> bool:
        def dfs(node, min_, max_):
            if node is None:
                return True
            if node.val >= min_ or node.val <= max_:
                return False
            
            return dfs(node.left, min_, node.val) and dfs(node.right, node.val, max_)
        
        return dfs(root, float('-inf'), float('inf'))
            
