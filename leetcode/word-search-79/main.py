# You need to know that this is a dfs problem not bfs and you need to do it recursivley not iterativly 
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        H, W = len(board), len(board[0])
        v = set()

        def dfs(x, y, pos):
            if (x >= H or x < 0) or (y >= W or y < 0):
                return False
            
            if (x, y) in v:
                return False
            

            if pos < len(word) and word[pos] != board[x][y]:
                return False
            
            if pos == len(word) - 1:
                return True
            v.add((x,y))
            
            res =  dfs(x+1, y, pos + 1) or dfs(x-1, y, pos + 1) or dfs(x, y+1, pos + 1) or dfs(x, y-1, pos + 1)
            v.remove((x,y))
            
            return res

        for i in range(H):
            for j in range(W):
                if board[i][j] == word[0]:
                    v = set()
                    # v.add((i, j))
                    res = dfs(i, j, 0)
                    if res:
                        return res
        
        return False


