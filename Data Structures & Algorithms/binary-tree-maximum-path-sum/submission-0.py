# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_val = root.val

        def dfs(node):
            nonlocal max_val;
            
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            current_max_val = node.val + left + right
            max_val = max(max_val, current_max_val)

            val_to_parent = node.val + max(left, right)
            return val_to_parent if val_to_parent > 0 else 0

        dfs(root)

        return max_val