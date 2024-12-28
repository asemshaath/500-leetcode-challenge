class Solution:
    def climbStairs(self, n: int) -> int:

        tracker = [1, 2]
        if n <=2:
            return tracker[n - 1]
        curr = 3

        while curr <= n:
            tmp1 = tracker[1]
            tmp2 = sum(tracker)
            curr += 1
            tracker = [tmp1, tmp2]
        return tracker[1]
