# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        res = []

        while q:
            qLen = len(q)
            curr_level = []

            for _ in range(qLen):
                node = q.popleft()
                if node:
                    curr_level.append(node.val)

                    q.append(node.left)
                    q.append(node.right)
            
            if curr_level:
                res.append(curr_level)
        
        return res

