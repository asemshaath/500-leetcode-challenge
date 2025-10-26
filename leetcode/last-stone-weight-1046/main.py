class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = stones.copy()
        h = [s * -1 for s in h]
        heapq.heapify(h)

        while len(h) > 1:
            stone1 = heapq.heappop(h) * -1
            stone2 = heapq.heappop(h) * -1

            res = abs(stone1 - stone2)

            if res != 0:
                heapq.heappush(h, res * -1)
        
        if len(h) == 1:
            return h[0] * -1
        return 0

