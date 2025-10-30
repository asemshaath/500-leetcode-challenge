class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        def h(i, subres):

            if i == len(nums):
                res.append(subres.copy())
                return
            
            if i > len(nums):
                return

            h(i + 1, subres + [nums[i]])

            new_i = i
            while new_i < len(nums) and nums[new_i] == nums[i]:
                new_i += 1

            h(new_i, subres)
        
        h(0, [])
        return res
