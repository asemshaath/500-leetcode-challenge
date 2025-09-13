class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = []
        M = len(grid)
        total = 0
        
        # build columns list to check in O(1)



        # cost O(N)
        for i in range(M):
            res = []
            for j in range(M):
                res.append(grid[j][i])
            cols.append(res)

        for i in range(M):
            for j in range(M):
                if cols[j] == grid[i]:
                    total += 1
        
        return total

        
