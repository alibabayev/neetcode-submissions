# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        preorder_index = 0
        left = 0
        right = len(inorder) - 1

        
        def build(left, right):
            nonlocal preorder_index

            if left > right:
                return None
            
            val = preorder[preorder_index]
            mid = inorder_map[val]
            node = TreeNode(val)
            preorder_index += 1
            
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)

            return node

        
        return build(left, right)


# preorder = [1,2,3,4], inorder = [2,1,3,4]
# Output: [1,2,3,null,null,null,4]