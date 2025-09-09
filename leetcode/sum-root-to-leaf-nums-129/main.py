# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        paths = []

        def traverese(node, path):
            if not node:
                return

            new_path = path + [str(node.val)]

            if not node.left and not node.right:
                paths.append(int("".join(new_path)))
            else:
                traverese(node.left, new_path)
                traverese(node.right, new_path)
        
        traverese(root, [])

        return sum(paths)
