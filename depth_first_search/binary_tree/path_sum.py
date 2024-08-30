"""
find if tree has root-to-leaf path where all the values along that path sum to the target
"""
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, nodes: Node, target: int) -> bool:
        if nodes is None:
            return False
        
        if nodes.left is None and nodes.right is None:
            return target == nodes.val
        
        left = self.pathSum(nodes.left, target - nodes.val)
        right = self.pathSum(nodes.right, target - nodes.val)

        return left or right
    