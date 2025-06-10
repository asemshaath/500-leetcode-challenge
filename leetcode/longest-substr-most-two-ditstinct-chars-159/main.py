class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        L = 0
        letters = dict()
        res = 0

        for R in range(len(s)):
            letters[s[R]] = letters.get(s[R], 0) + 1
            while len(letters) > 2:
                letters[s[L]] -= 1
                if letters[s[L]] == 0:
                    del letters[s[L]]
                L += 1
            res = max(res, R - L + 1)
        
        return res



