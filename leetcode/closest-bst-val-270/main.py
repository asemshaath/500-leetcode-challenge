# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val

        curr = root
        while curr:
            if abs(curr.val - target) < abs(closest - target):
                closest = curr.val
            elif abs(curr.val - target) == abs(closest - target):
                closest = min(closest, curr.val)

            curr = curr.left if curr.val > target else curr.right

        return closest
                
