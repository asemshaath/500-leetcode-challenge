# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        stack = []
        curr = root
        tree_lst = [] #inorder

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            tree_lst.append(curr.val)
            curr = curr.right
        print(tree_lst)
        
        for i in range(1, len(tree_lst)):
            if tree_lst[i-1] >= tree_lst[i]:
                return False

        return True

