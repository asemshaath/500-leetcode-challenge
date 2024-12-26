class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negatives = [n * n for n in nums if n < 0]
        negatives.reverse()
        positives = [n * n for n in nums if n >= 0]
        merged = []
        n, p = 0, 0
        ln, lp = len(negatives), len(positives)

        while n < ln and p < lp:
            if negatives[n] > positives[p]:
                merged.append(positives[p])
                p += 1
            else:
                merged.append(negatives[n])
                n += 1

        merged.extend(negatives[n:])
        merged.extend(positives[p:])

        return merged
