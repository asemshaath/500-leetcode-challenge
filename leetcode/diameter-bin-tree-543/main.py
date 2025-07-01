# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = [0]

        def height(node):
            if node:
                left_h = height(node.left)
                right_h = height(node.right)
                diameter[0] = max(diameter[0], left_h + right_h)
                return max(left_h, right_h) + 1
            return 0
            
        h = height(root)
        return diameter[0]
