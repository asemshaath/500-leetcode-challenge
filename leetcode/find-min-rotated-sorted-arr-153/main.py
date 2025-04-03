class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while r - l > 1:
            mid = (r + l) // 2
            if nums[mid] < nums[l]:
                r = mid
            elif nums[mid] > nums[l] and nums[mid] < nums[r]:
                r = mid
            else:
                l = mid
        return min(nums[l], nums[r])

            


# update to better solution

class Solution2:
    def findMin(self, nums: List[int]) -> int:
        # 4,5,6,0,1,2
        # l     m   r
        # 
        # l < r return l

        l = 0 
        r = len(nums) - 1
        mini = 5000000

        while l <= r:
            if nums[l] <= nums[r]:
                mini = min(mini, nums[l])
                return mini
            
            m = (r + l) // 2

            if nums[m] >= nums[l]:
                mini = min(mini, nums[m])
                l = m + 1
            else:
                mini = min(mini, nums[m])
                r = m - 1
        return nums[l]


