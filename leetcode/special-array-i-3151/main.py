class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        L = len(nums)
        if L < 2:
            return True

        first = 0
        sec = 1

        while sec < L:
            if nums[first] % 2 == nums[sec] % 2:
                return False
            first += 1
            sec += 1
        
        return True
