# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good_nodes = [0]
        def traverese(node, path):
            
            if not node:
                return
            
            if len(path) == 0 or max(path) <= node.val:
                good_nodes[0] += 1

            new_path = path + [node.val]
            traverese(node.left, new_path)
            traverese(node.right, new_path)

        traverese(root, [])

        return good_nodes[0]
