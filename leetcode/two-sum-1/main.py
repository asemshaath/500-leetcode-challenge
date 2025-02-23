class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2,7,11,15
        # 7,2,-2,-6

        hm = {nums[i]:i for i in range(len(nums))}

        for i, n in enumerate(nums):
            if target - n in hm and n + nums[hm[target - n]] == target and i != hm[target - n]:
                return [i, hm[target - n]]
        return []


        
