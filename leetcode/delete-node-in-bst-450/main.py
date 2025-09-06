# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if root:

            if root.val > key:
                root.left = self.deleteNode(root.left, key)
            elif root.val < key:
                root.right = self.deleteNode(root.right, key)
            else:

                # easy case

                if root.left is None:
                    root = root.right
                elif root.right is None:
                    root = root.left
                else:
                    min_node = self.get_minimum_node(root.right)
                    self.deleteNode(root, min_node.val)
                    root.val = min_node.val
        return root
    
    def get_minimum_node(self, root):
        
        curr = root

        while curr and curr.left:
            curr = curr.left
        
        return curr
