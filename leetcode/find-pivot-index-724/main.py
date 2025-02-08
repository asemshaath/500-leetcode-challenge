class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        #             
        # 1,8,11,17,22,28
        # 1,7,3,6,5,6
        # 28,27,20,17,11,6
        # 
        #                    
        # -1, -2, -3, -4, -5, -5
        # -1,-1,-1,-1,-1,0
        # -5, -4, -3 ,-2 ,-1 , 0    

        # l = 0
        lsum = 0
        rsum = sum(nums)

        for l in range(len(nums)):
            lsum += nums[l]
            
            if lsum == rsum:
                return l
            
            rsum -= nums[l]
        
        return -1






