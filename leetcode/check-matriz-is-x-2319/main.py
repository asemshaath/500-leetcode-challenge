class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        
        N = len(grid)

        for i in range(N):
            for j in range(N):

                if self.is_in_diognal(i, j, N) and grid[i][j] == 0:
                    return False
                
                if not self.is_in_diognal(i,j,N) and grid[i][j] != 0:
                    return False

        return True
    

    def is_in_diognal(self, i, j, n):
        if i == j:
            return True
        
        # (1,2) n = 4 turn to (1,1)
        # (0,0) -> (0,3) given n = 4 last is 3
        # (1,2) -> (1,1)

        j_reflect = n - j - 1
        if i == j_reflect:
            return True
        return False
        


