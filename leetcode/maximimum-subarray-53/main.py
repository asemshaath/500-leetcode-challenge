    def maxSubArray(self, nums: List[int]) -> int:
        # [-2,1,-3,4,-1,2,1,-5,4]
        #  0  1  2 3  4 5 6  7 8
        #                            
        
        maxim = nums[0]
        curr_max = 0

        for i in range(len(nums)):
            if curr_max < 0:
                curr_max = 0
            
            curr_max += nums[i]
            if curr_max >= maxim:
                maxim = curr_max
        
        return maxim
