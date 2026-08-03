# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        is_subtree = False
        if root.val == subRoot.val:
            is_subtree = self.checkSubtree(root, subRoot)

        return is_subtree or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    
    def checkSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not root and not subRoot:
                return True

            if not root or not subRoot or root.val != subRoot.val:
                return False

            return self.checkSubtree(root.left, subRoot.left) and self.checkSubtree(root.right, subRoot.right) 
        


        
            
