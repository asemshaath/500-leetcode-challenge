class Solution:
    def minimumLength(self, s: str) -> int:
        occurances = {}

        for c in s:
            if occurances.get(c):
                occurances[c] += 1
                if occurances[c] >= 3:
                    occurances[c] -= 2

            else:
                occurances[c] = 1

        p = [v for _, v in list(occurances.items())]
    
        return sum(p)
