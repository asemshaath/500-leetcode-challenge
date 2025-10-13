class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def h(i, curr_sum, paths):
            if i >= len(candidates):
                return
            
            if curr_sum == target:
                res.append(paths)
                return
            
            if curr_sum > target:
                return
            
            new_paths = paths + [candidates[i]]
            h(i, curr_sum + candidates[i], new_paths)
            h(i+1, curr_sum, paths.copy())
        
        h(0, 0, [])

        return res

