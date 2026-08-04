# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
            
        count = 0

        def dfs(max_val: int, root: TreeNode) -> None:
            nonlocal count;

            if not root:
                return None
            
            if root.val >= max_val:
                count += 1
            
            max_val = max(max_val, root.val)
            
            dfs(max_val, root.left)
            dfs(max_val, root.right)

        
        dfs(root.val, root)

        return count

        