# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False

        def checkSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not root and not subRoot:
                return True

            if not root or not subRoot or root.val != subRoot.val:
                return False

            
            return checkSubtree(root.left, subRoot.left) and checkSubtree(root.right, subRoot.right) 
        
        is_subtree = False
        if root.val == subRoot.val:
            is_subtree = checkSubtree(root, subRoot)

        return is_subtree or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        


        
            
