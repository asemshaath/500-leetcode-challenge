class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        1:[]
        2:[[1,1], [3,1]]
        3:[[4,1]]
        4:[]
        """

        LARGE_INT = 900000000
        graph = self.build_graph(times, n)

        distance_from_k = [LARGE_INT] * (n + 1)
        visited = set()
        q = [(0, k)]
        distance_from_k[k] = 0

        while q:
            length, c = heapq.heappop(q)
            # visited.add(c)

            if length > distance_from_k[c]:
                continue
                
            for d, w in graph[c]:
                new_dist = length + w
                if new_dist < distance_from_k[c]:
                    distance_from_k[c] = new_dist
                    heapq.heappush(q, (new_dist, d))
                # visited.add(d)
        

        res = max(distance_from_k[1:])
        if res < LARGE_INT:
            return res
        return -1

    def build_graph(self, times, n):

        g = {i:[] for i in range(1,n+1)}
        
        for src, dest, w in times:
            g[src].append([dest, w])
        return g
