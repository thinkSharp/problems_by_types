"""
In order to calculate tilt, we have to take the sum of left and some of right and find the absolute
distance

Appraoch: using recursive function, local vairable to store the tilt and return sum in local recursive function

Time complexity should be O(n) number of nodes
Space complexity should be O(n) as we would create stack frame for each recursive call
"""
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def calculate_tilt(self, root: Node):
        tilt = 0
        def dfs(node: Node):
            nonlocal tilt
            if node is None:
                return 0
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            tilt += abs(left_sum - right_sum)

            return node.val + left_sum + right_sum
        dfs(root)
        return tilt