class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        last = 0
        {
            0:2
            1:2
        }
        1011001001
        l
         r
        last=1
        00100011
        l
           r
        last=1
        """

        groups = [0]
        L = len(s)
        last = s[0]
        res = 0

        for i in range(L):
            if s[i] == last:
                groups[-1] += 1
            else:
                last = s[i]
                groups.append(1)
        
        for i in range(1, len(groups)):
            res += min(groups[i], groups[i-1])
        
        return res
            

