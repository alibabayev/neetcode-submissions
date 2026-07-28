"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copied = {}

        if not node:
            return None
        
        def dfs(node):
            if not node:
                return None
            
            
            copy = Node(node.val)
            copied[node] = copy
            for nei in node.neighbors:
                if nei in copied:
                    copy.neighbors.append(copied[nei])
                else:
                    copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node)


        
    
        
        