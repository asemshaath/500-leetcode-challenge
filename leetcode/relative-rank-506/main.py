class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """
        [5,4,3]
        """

        cpr = score.copy()
        cpr.sort()
        rank_map = {}
        L = len(score)

        for i in reversed(range(len(cpr))):
            if L - i == 1:
                rank_map[cpr[i]] = "Gold Medal"
            elif L - i == 2:
                rank_map[cpr[i]] = "Silver Medal"
            elif L - i == 3:
                rank_map[cpr[i]] = "Bronze Medal"
            else:
                rank_map[cpr[i]] = str(L - i)
        
        res = [rank_map[n] for n in score]
        return res
