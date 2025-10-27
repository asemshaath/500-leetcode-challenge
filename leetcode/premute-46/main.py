class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        s = set()

        def h(paths):

            if len(paths) == len(nums):
                res.append(paths.copy())
                return

            for i in range(len(nums)):
                if nums[i] not in s:
                    paths.append(nums[i])
                    s.add(nums[i])
                    h(paths.copy())
                    s.remove(nums[i])
                    paths.pop()

        h([])
        return res
