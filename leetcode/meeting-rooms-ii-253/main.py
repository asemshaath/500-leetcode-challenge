class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        c_intervals = intervals.copy()
        c_intervals.sort()
        num_rooms = 0

        pq = []

        for i in range(len(intervals)):
            s, e = c_intervals[i]

            if len(pq) > 0:
                if s < pq[0]:
                    heapq.heappush(pq, e)
                else:
                    heapq.heappop(pq)
                    heapq.heappush(pq, e)
            else:
                heapq.heappush(pq, e)

            num_rooms = max(num_rooms, len(pq))


        return num_rooms
        
