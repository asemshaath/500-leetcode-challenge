class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        pl, pr = 0, 0

        for i in range(len(s)):
            # odd check
            l,r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if pr - pl + 1 < r - l + 1:
                    pl, pr = l, r
                l -= 1
                r += 1
            
            # even check
            l, r = i, i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if pr - pl + 1 < r - l + 1:
                    pl, pr = l, r
                l -= 1
                r += 1

        return s[pl:pr+1]
            



        


