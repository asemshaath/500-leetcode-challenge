class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        """
            nums = [2, 2, 3, 3, 3, 4]

            occ = {
                2:2,
                3:3,
                4:1,
            }

            iterate through occ:
            if pick 2:
                M = 2
                update_occ -> 3 and 1 is removed
                and occ[2]-=1
            else:

        """

        occ = dict()
        earnings = 0

        for n in nums:
            if occ.get(n):
                occ[n] += 1
            else:
                occ[n] = 1

        def backtrack(occ_dict, _earnings):
            nonlocal earnings
            earnings = max(earnings, _earnings)

            for k,v in occ_dict.items():
                # pick
                occ_cp = occ_dict.copy()
                occ_cp[k] -= 1
                if occ_cp[k] == 0:
                    occ_cp.pop(k)

                if occ_cp.get(k - 1):
                    occ_cp.pop(k-1)
                
                if occ_cp.get(k+1):
                    occ_cp.pop(k+1)
                
                backtrack(occ_cp, _earnings + k)

                # skip
                # no code needed

        
        backtrack(occ.copy(), earnings)
        return earnings










