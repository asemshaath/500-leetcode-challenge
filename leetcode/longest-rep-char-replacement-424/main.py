class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        occ = dict()
        res = 0

        for R in range(len(s)):
            occ[s[R]] = occ.get(s[R], 0) + 1
            max_occ = max(list(occ.values()))
            if (R - L + 1) - max_occ <= k:
                res = max(res, R - L + 1)
            else:
                while (R - L + 1) - max_occ > k:
                    occ[s[L]] -= 1
                    L += 1


        return res
