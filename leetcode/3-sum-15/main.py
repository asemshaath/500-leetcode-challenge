class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -1,0,1,2,-1,-4
        # -4,-1,-1,0,1,2
        #     l  m     r    
        
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while right - left > 0:
                three_sum = nums[right] + nums[left] + n
                if three_sum == 0:
                    res.append([nums[right], nums[left], n])
                    left += 1
                    while nums[left] == nums[left - 1] and right - left > 0:
                        left += 1

                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1
            
        return res
            

