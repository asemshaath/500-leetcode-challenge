class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        abccccdd
        a 1
        b 1
        c 4
        d 2

        """

        res = 0
        occurrances = defaultdict(int)

        for c in s:
            occurrances[c] += 1
        
        has_odd = False

        for k, v in occurrances.items():
            if v >= 2:
                res += (v // 2 * 2)
            if v % 2 != 0 and not has_odd:
                res += 1
                has_odd = True


        return res
        
