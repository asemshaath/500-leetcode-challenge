import heapq
class MedianFinder:

    
    def __init__(self):
        self.small = [] # maxheap
        self.large = [] # minheap


    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            ne_val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * ne_val)

        if len(self.large) - len(self.small) > 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        
        if len(self.small) - len(self.large) > 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]

        if len(self.large) < len(self.small):
            return -1 * self.small[0]

        return ((-1 * self.small[0]) + self.large[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
