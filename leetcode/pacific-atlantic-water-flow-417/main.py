class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """

        """

        pacific_set = set()
        atlantic_set = set()
        M = len(heights)
        N = len(heights[0])
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        res = []

        def traverse(ocean_name, x, y):
            if ocean_name == "pacific":
                v = pacific_set
            elif ocean_name == "atlantic":
                v = atlantic_set
            else:
                return

            if (x, y) in v:
                return
            
            pq = deque([(x, y)])
            v.add((x, y))

            while pq:
                tx, ty = pq.popleft()
                # v.add((tx, ty))

                for dx, dy in directions:
                    ax = dx + tx
                    ay = dy + ty
                    if ax >= 0 and ax < M and ay >= 0 and ay < N and (ax, ay) not in v:
                        if heights[tx][ty] <= heights[ax][ay]:
                            v.add((ax, ay))
                            pq.append((ax, ay))
                
        # build pacific set
        for i in range(N):
            traverse("pacific", 0, i)
        for i in range(M):
            traverse("pacific", i, 0)

        # build atlantic ocean
        for i in range(N):
            traverse("atlantic", M - 1, i)

        for i in range(M):
            traverse("atlantic", i, N - 1)

        for x, y in pacific_set:
            if (x, y) in atlantic_set:
                res.append([x, y])
        
        return res
