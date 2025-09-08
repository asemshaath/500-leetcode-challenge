# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])
        # q: 5, 4
        # res: [1]
        while q:
            qLen = len(q)
            right_most = None

            for _ in range(qLen):
                node = q.popleft()

                if node:
                    right_most = node
                    q.append(node.left)
                    q.append(node.right)
            
            if right_most:
                res.append(right_most.val)
        
        return res
            
