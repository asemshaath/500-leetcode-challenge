class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def h(i, paths, curr_sum):
            
            if curr_sum == target:
                res.append(paths.copy())
                return
            
            if curr_sum > target:
                return

            if i >= len(candidates):
                return

            h(i + 1, paths + [candidates[i]], curr_sum + candidates[i])
            new_i = i

            while new_i < len(candidates) and candidates[new_i] == candidates[i]:
                new_i += 1

            h(new_i, paths, curr_sum)


        h(0, [], 0)
        return res
