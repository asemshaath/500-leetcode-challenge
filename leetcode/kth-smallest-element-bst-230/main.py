# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        arr = []

        def rec_h(node):
            if node:
                rec_h(node.left)
                arr.append(node.val)
                rec_h(node.right)
        
        rec_h(root)

        return arr[k-1]
