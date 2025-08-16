class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # find the pivot index (lowest number)
        # if left > right => pivot is between 
        l, r = 0, len(nums) - 1
        m = (r+l)// 2

        while r > l:
            m = (r+l)// 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l
        l, r = 0, len(nums) - 1

        while r >= l:
            m = (l+r)//2
            mp = m + pivot
            mp = mp - len(nums) if mp >= len(nums) else mp
            if nums[mp] < target:
                l = m + 1
            elif nums[mp] > target:
                r = m - 1
            else:
                return mp
        
        return -1
