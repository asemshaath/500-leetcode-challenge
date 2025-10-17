class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        heapq.heapify(h)

        for x, y in points:
            d = math.sqrt(x**2 + y**2)
            heapq.heappush(h, (d, x, y))
        
        

        res = []
        
        for _ in range(k):
            _, rx, ry = heapq.heappop(h)
            res.append([rx, ry])

        return res
