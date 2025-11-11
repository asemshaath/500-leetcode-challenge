class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        0 representing an empty cell
        1 representing a fresh orange
        2 representing a rotten orange
        """

        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        q = deque()
        R = len(grid)
        C = len(grid[0])
        time = -1
        fresh_oranges = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1            

        if fresh_oranges <= 0 and len(q) == 0:
            return 0

        while q:
            lenq = len(q)

            for _ in range(lenq):
                x, y = q.popleft()
                
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if nx >= 0 and nx < R and ny >= 0 and ny < C:
                        if grid[nx][ny] == 1:
                            fresh_oranges -= 1
                            q.append((nx, ny))
                            grid[nx][ny] = 2
                            # s.add((nx, ny))
            time += 1
        

        if fresh_oranges > 0:
            return -1

        return time


        



