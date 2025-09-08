# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        total = [0]

        def rec_h(node):
            if not node:
                return
            
            if node.left and not node.left.right and not node.left.left:
                total[0] += node.left.val

            rec_h(node.left)
            rec_h(node.right)
        
        rec_h(root)
        return total[0]
