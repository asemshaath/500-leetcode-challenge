class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        # 2, 0 -> 3, 0
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        R = len(rooms)
        C = len(rooms[0])
        q = deque()
        v = set()

        for i in range(R):
            for j in range(C):
                if rooms[i][j] == 0:
                    q.append((i, j))
                    v.add((i, j))
        
        # do bfs simolutaniously
        counter = 0
        while q:
            qlen = len(q)
            for _ in range(qlen):
                x, y = q.popleft()
                rooms[x][y] = counter

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if nx >= 0 and nx < R and ny >= 0 and ny < C and rooms[nx][ny] != -1 and (nx, ny) not in v:
                        q.append((nx, ny))
                        v.add((nx, ny))
            counter += 1

