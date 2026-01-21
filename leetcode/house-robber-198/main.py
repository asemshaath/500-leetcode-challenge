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



class Solution2:
    def rob(self, nums: List[int]) -> int:
        """
        [2,1,1,2]
             i
        [2,2]
        
        """

        if len(nums) == 1:
            return nums[0]
        
        dp = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            new_amount = max(dp[i-1], dp[i - 2] + nums[i])
            dp.append(new_amount)
        
        return dp[-1]


            

