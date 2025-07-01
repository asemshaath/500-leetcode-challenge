# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def height(node):
            
            if node:
                right_h = height(node.right)
                left_h = height(node.left)
                if abs(left_h - right_h) > 1:
                    balanced[0] = False
                return 1 + max(left_h, right_h)
            return 0
        
        h =  height(root)
        print(h)
        return balanced[0]
        


        
