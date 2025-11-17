class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        [7,10],[2,4]

        [2,4], [7,10]
        
        """

        p1, p2 = 0, 1
        intervals.sort()
        
        while p2 < len(intervals):
            s1, e1 = intervals[p1]
            s2, e2 = intervals[p2]

            if e1 > s2:
                return False
            p1 += 1
            p2 += 1
            
        return True
                
