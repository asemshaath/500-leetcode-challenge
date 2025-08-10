# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        same_tree_res = [True]
        def same_tree(n1, n2):
            if n1 and n2:
                if n1.val == n2.val:
                    same_tree(n1.left, n2.left)
                    same_tree(n1.right, n2.right)
                else:
                    same_tree_res[0] = False
            elif n1 and not n2 or n2 and not n1:
                same_tree_res[0] = False
        
        is_sub_tree = [False]

        def rec_h(r, sr):
            if r and sr:
                if r.val == sr.val:
                    same_tree(r, sr)
                    if same_tree_res[0]:
                        is_sub_tree[0] = same_tree_res[0]
                    else:
                        same_tree_res[0] = True
                # else:
                rec_h(r.left, sr)
                rec_h(r.right, sr)
            

        rec_h(root, subRoot)
        return is_sub_tree[0]

