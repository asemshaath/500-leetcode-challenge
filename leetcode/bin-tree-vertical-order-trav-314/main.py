# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # (-1, 9), (1, 8)
        nodes_cols = []
        cols_grid = dict()
        q = deque([(0, root)])

        if not root:
            return []
        while q:
            qlen = len(q)
            level, node = q.popleft()

            if not node:
                continue 
            if cols_grid.get(level):
                cols_grid[level].append(node.val)
            else:
                cols_grid[level] = [node.val]
            
            q.append((level - 1, node.left))
            q.append((level + 1, node.right))
            # for _ in range(len(qlen)):


        print(cols_grid)
        print(cols_grid.keys())
        min_key = min(list(cols_grid.keys()))
        to_zero_base = abs(min_key)
        print(to_zero_base)
        res = [None] * len(list(cols_grid.keys()))

        for k, v in cols_grid.items():
            res[k+to_zero_base] = v

        return res
