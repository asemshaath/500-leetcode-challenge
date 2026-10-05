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


class Solution3:
    def findMin(self, nums: List[int]) -> int:
        """
        3,4,5,1,2

        nums[l] = 3
        nums[r] = 2

        Unrotated arrays must have nums[r] > nums[l]
        return nums[0]
        else

        l = 0
        r = 4
        m = 4 // 2 = 2

        3,4,5,1,2
              l r

        2,4,5,6,7,0,1

        4,5,6,7,0,1,2
              l     r

        """

        l = 0
        r = len(nums) - 1

        if nums[l] < nums[r]:
            return nums[0]

        while r - l > 1:
            m = (l + r) // 2

            if nums[m] > nums[l]:
                l = m
            else:
                r = m
        
        return nums[r]

