# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack = []
        res = []

        def rec_h(node, s):
            if not node:
                return
            

            new_path = s + [(str(node.val))]

            if not node.left and not node.right:
                res.append(new_path)
            else:
                rec_h(node.left, new_path)
                rec_h(node.right, new_path)

        rec_h(root, [])

        print(res)
        new_res = []

        for r in res:
            new_res.append("->".join(r))

        return new_res
