class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return self.rob_h(nums, 0, {})


    def rob_h(self, nums, start, memo):
        first = start + 1
        sec = start + 2

        if start >= len(nums):
            return 0

        if start in memo:
            return memo[start]

        memo[start] = max(
            self.rob_h(nums, first, memo), self.rob_h(nums, sec, memo) + nums[start]
        )

        return memo[start]

