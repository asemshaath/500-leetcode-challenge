# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder = [3,9,20,15,7] 
        # inorder = [9,3,15,20,7]

        root = None
        if inorder and preorder:
            root = TreeNode(preorder[0])

            parent_val = preorder[0]
            mid = inorder.index(parent_val)
            left_subtree_inorder = inorder[:mid]
            right_subtree_inorder = inorder[mid + 1:]

            left_subtree_preorder = preorder[1:len(left_subtree_inorder)+1]
            right_subtree_preorder = preorder[len(left_subtree_inorder)+1:]

            root.left = self.buildTree(left_subtree_preorder, left_subtree_inorder)
            root.right = self.buildTree(right_subtree_preorder, right_subtree_inorder)

        return root
