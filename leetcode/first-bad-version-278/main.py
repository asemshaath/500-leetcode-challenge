# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        p = (r + l) // 2
        
        while l < r:
            p = (r + l) // 2
            p_res = isBadVersion(p)

            if p_res:
                r = p 
            else:
                l = p + 1

            if l == r:
                return l
        
        return l
            
