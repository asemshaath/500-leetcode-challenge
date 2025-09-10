# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        total = [0]

        def traverse(node):
            if not node:
                return
            
            if node.val >= low and node.val <= high:
                total[0] += node.val

            if node.val >= low:
                traverse(node.left)
            if node.val <= high:
                traverse(node.right)
        
        traverse(root)
        return total[0]
    
