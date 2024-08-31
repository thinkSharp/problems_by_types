"""
given reference to a variable node, which is part of an undirected connected graph,
write a function to return adjacency list in dictionary form.

Solution Approach:
- treverse through the entire graph
- keep track of visited nodes
- build a dictionary of key and values
    - key is Node. Val
    - value is neighbors Val

Time Complexity O(n) where n is number of nodes
Space Complexity O(n) to store visited nodes
"""
class IntGraphNode:
    def __init__(self, value = 0, neighbors = None):
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def copy_graph(self, node: IntGraphNode):
        adj_map = {}

        def dfs(node: IntGraphNode):
            if node.value in adj_map:
                return
            
            adj_map[node.value] = [n.value for n in node.neighbors]
            for neighbor in node.neighbors:
                dfs(neighbor)
        
        if node:
            dfs(node)

        return adj_map