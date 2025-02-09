import heapq

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        L = len(grid)
        W = len(grid[0])
        pq = []
        vistied = set()
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += 1
        
        res = res * 4

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in vistied:
                    # traverse bfs
                    # mark it as visted
                    # check adjecents
                    # push valid ajdcents to the queue
                    heappush(pq, (i, j))

                    while pq:
                        x, y = heappop(pq)
                        if (x, y) not in vistied:
                            vistied.add((x, y))
                            adj = [(x - 1, y), (x,y - 1), (x + 1,y), (x,y + 1)]
                            adj = [(px, py) for px, py in adj if px >= 0 and px < L and py >= 0 and py < W]
                            adj = [(px, py) for px, py in adj if grid[px][py] == 1]
                            res -= len(adj)
                            
                            for px, py  in adj:
                                if (px, py) not in vistied:
                                    heappush(pq, (px, py))
                    
        return res








