    def numIslands(self, grid: List[List[str]]) -> int:
        
        num_islands = 0
        visited = set()
        stack = []


        def dfs():
            while stack:
                i, j = stack.pop()
                visited.add((i, j))
                adj = [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]

                for a in adj:
                    ip, jp = a
                    if isValidIndex(ip, jp) and (ip, jp) not in visited and grid[ip][jp] == "1":
                        stack.append(a)


        
        def isValidIndex(i, j):
            if i < 0 or j < 0:
                return False
            elif i >= len(grid): 
                return False
            elif j >= len(grid[0]):
                return False
            return True

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                curr = grid[i][j]
                if grid[i][j] == "1" and (i, j) not in visited:
                    stack.append((i, j))
                    dfs()
                    num_islands += 1

        return num_islands




# new solution for recursive approach

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        num_islands = 0
        visited = set()

        def dfs(x, y):
            
            if (not isValidIndex(x, y) or
                grid[x][y] != "1" or
                (x, y) in visited):
                return 

            visited.add((x, y))
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            

        
        def isValidIndex(i, j):
            if i < 0 or j < 0:
                return False
            elif i >= len(grid): 
                return False
            elif j >= len(grid[0]):
                return False
            return True

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                curr = grid[i][j]
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    num_islands += 1

        return num_islands



# another attempt after long time

class Solution3:
    def numIslands(self, grid: List[List[str]]) -> int:
        """

        dfs -> stack

        iterate through every unit
        if land, run traverse


        """

        num_islands = 0
        visited = set()
        M = len(grid)
        N = len(grid[0])

        def traverse(x, y):
            stack = [(x, y)]
        
            while stack:
                xi, yi = stack.pop()
                adj = [(xi+1, yi), (xi, yi+1), (xi-1, yi), (xi, yi-1)]
                adj = [(i, j) for i, j in adj if i >= 0 and i < M and j >= 0 and j < N]
                valid_adj = [(i,j) for i, j in adj if grid[i][j] == '1' and (i, j) not in visited]

                visited.add((xi, yi))
                stack.extend(valid_adj)

        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1" and (i,j) not in visited:
                    traverse(i, j)
                    num_islands+=1

        return num_islands
