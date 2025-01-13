class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        L = len(s)
        lw = 0
        p = L - 1

        while p >= 0:
            if s[p] == ' ' and lw == 0:
                p -= 1
            elif s[p] == ' ' and lw != 0:
                break
            else:
                lw += 1
                p -= 1
        return lw
