# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def height(root: Optional[TreeNode]) -> int:
            nonlocal balanced;

            if not balanced or not root:
                return 0
            
            left_height = height(root.left)
            right_height = height(root.right)

            if balanced:
                balanced = abs(left_height - right_height) <= 1

            return 1 + max(left_height, right_height)
        
        height(root)
        
        return balanced