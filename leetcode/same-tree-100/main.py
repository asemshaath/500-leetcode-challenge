# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        not_same = [True]
        def rec_h(n1, n2):
            if n1 and n2:
                if n1.val != n2.val:
                    not_same[0] = False
                rec_h(n1.left, n2.left)
                rec_h(n1.right, n2.right)
            elif n1 and not n2 or n2 and not n1:
                not_same[0] = False

        rec_h(p, q)
        return not_same[0]

