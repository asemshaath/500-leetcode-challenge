class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        s = set() #index

        def h(paths):
            
            if len(paths) == len(nums):
                res.add(",".join(paths.copy()))
                return

            for i in range(len(nums)):
                if i not in s:
                    paths.append(str(nums[i]))
                    s.add(i)
                    h(paths.copy())
                    paths.pop()
                    s.remove(i)

        h([])
        res = [p.split(',') for p in list(res)]
        for i in range(len(res)):
            for j in range(len(res[i])):
                res[i][j] = int(res[i][j])
        
        return res
