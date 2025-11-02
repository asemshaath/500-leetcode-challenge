class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        [0,1,1],
        [1,1,1],
        [1,1,0]

        [
            [0,0,0],
            [1,0,0],
            [1,1,0]
        ]

        [
            [0,0,0],
            [0,1,0],
            [0,0,0]
        ]

        [
            [1,0,0],
            [1,1,0],
            [1,1,0]]

        """
        N = len(grid)
        if grid[N-1][N-1] != 0 or grid[0][0] != 0:
            return -1
        

        directions = [[0,1], [1,0], [-1,0], [0,-1], [1,1], [-1,-1], [1,-1], [-1, 1]]
        goal = (N-1, N-1)
        q = deque([(0, 0, 1)])
        grid[0][0] = -1
        
        while q:
            x, y, d = q.popleft()
            if (x, y) ==  goal:
                return d

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if nx >= 0 and nx < N and ny >= 0 and ny < N and grid[nx][ny] == 0:
                    q.append((nx, ny, d + 1))
                    grid[nx][ny] = -1

        return -1




