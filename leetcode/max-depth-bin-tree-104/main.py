# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def helper(node, depth):
            if node:
                left_depth = helper(node.left, depth + 1)
                right_depth = helper(node.right, depth + 1)
                
                return max(left_depth, right_depth)
            return depth
        
        res = helper(root, 0)
        return res
