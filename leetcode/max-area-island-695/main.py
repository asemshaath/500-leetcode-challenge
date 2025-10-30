class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        L, W = len(grid), len(grid[0])
        stack = []
        visited = set()

        def get_valid_adj(adjs):
            r = []

            for x, y in adjs:
                if x < L and x >= 0 and y < W and y >= 0:
                    if grid[x][y] == 1 and (x, y) not in visited:
                        r.append((x, y))
            
            return r

        def get_area(x, y):
            stack.append((x, y))
            area = 0
            while stack:
                ax, ay = stack.pop()
                if (ax, ay) not in visited:
                    area += 1
                    visited.add((ax, ay))
                    adj = [(ax + 1, ay), (ax - 1, ay), (ax, ay + 1), (ax, ay - 1)]
                    adj = get_valid_adj(adj)
                    stack.extend(adj)
            return area

        for i in range(L):
            for j in range(W):
                if grid[i][j] == 1:
                    island_area = get_area(i, j)
                    res = max(res, island_area)

        return res
