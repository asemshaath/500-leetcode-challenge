class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        length = 0
        letters = set()

        for R in range(len(s)):
            if s[R] in letters:
                while s[R] in letters:
                    letters.remove(s[L])
                    L += 1
                letters.add(s[R])
            else:
                letters.add(s[R])
                length = max(R - L + 1, length)
        return length
