class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
         0 1 2 3 4
        [2,3,4,1,4]

        [3,2,1,0,4]
        stack = 1, (2)  



        [2,5,0,0]
        """


        stack = list(range(1, nums[0] + 1))
        visited = set()
        l = len(nums)

        if l == 1:
            return True

        while stack != []:
            top = stack.pop()
            if top == (l -1):
                return True
            elif top >= l or top in visited:
                continue
            else:
                visited.add(top)
                h = nums[top]
                new_steps = list(range(top + 1, top + h + 1))
                stack.extend(new_steps)
        
        return False




        
        

        
