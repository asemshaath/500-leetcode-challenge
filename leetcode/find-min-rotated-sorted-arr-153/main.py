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

            
