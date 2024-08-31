"""
path sum II wants us to return all the paths that exists from root to leaf that sum nodes equal to target
we can provide this solution multiple approach
- bottom up, start from leaf node and create list all all leaves
   - after recursive run, check all the sum and return the list
- top down approach, pass in remaining target to the dfs recursive function
   - once the leaf node is reached, check to see if val == remaining_target
   - if that's the case then add to the result list

- second approach is more effecient as we are not create multiple list or calculating sum for every list

"""
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSumII(self, root: Node, target: int) -> list[list[int]]:
        if root is None:
            return None
        def dfs(node: Node, remaining_target, paths):
            if node is None:
                return 
            paths.append(node.val)
            if node.left is None and node.right is None and remaining_target == node.val:
                results.append(paths.copy())
            else:
                dfs(node.left, remaining_target - node.val, paths)
                dfs(node.right, remaining_target - node.val, paths)

            paths.pop()
        
        results = []
        dfs(root, target, [])
        return results       