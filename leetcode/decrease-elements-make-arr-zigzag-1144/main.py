class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        
        n = len(nums)
        even = 0
        odd = 0

        for i in range(n):
            if i % 2 == 0:
                left = nums[i-1] if i-1 >= 0 else float("inf")
                right = nums[i+1] if i+1 < n else float("inf")

                t = min(left, right)
                if nums[i] >= t:
                    even += nums[i] - t + 1
        
            if i % 2 == 1:
                left = nums[i-1] if i-1 >= 0 else float("inf")
                right = nums[i+1] if i+1 < n else float("inf")

                t = min(left, right)
                if nums[i] >= t:
                    odd += nums[i] - t + 1

        return min(even, odd)


                
