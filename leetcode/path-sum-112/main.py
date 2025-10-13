# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def traverse(node, curr_sum):
            
            if node:
                if not node.left and not node.right:
                    # compare curr_sum to targetSum
                    if curr_sum + node.val == targetSum:
                        return True
                    else:
                        return False
                
                has_sum_l = traverse(node.left, curr_sum + node.val)
                has_sum_r = traverse(node.right, curr_sum + node.val)

                return has_sum_l or has_sum_r
            return False

        res = traverse(root, 0)
        return res
